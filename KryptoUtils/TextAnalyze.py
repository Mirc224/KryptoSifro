import KryptoUtils.TextTransform as KTrans
import KryptoUtils.KryptoMath as KMat
import KryptoUtils.General as KU
import itertools as it


def freq_analyze_to_count(text: str) -> dict:
    char_dict = {}
    unique_chars = set(text)
    for char in unique_chars:
        char_dict[char] = text.count(char)
    return char_dict


def freq_analyze_to_prob(text: str) -> dict:
    total = len(text)
    char_dict = {}
    unique_chars = set(text)
    for char in unique_chars:
        char_dict[char] = text.count(char ) /total
    return char_dict


def coincidence(text: str):
    prob = [0] * 26
    letter_count = [0] * 26
    total = 0
    transformed_text = text.upper()

    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        unique_letter_count = transformed_text.count(letter)
        letter_count[ord(letter) - ord('A')] = unique_letter_count
        total += unique_letter_count

    koinc1, koinc2 = 0, 0
    for i in range(26):
        koinc1 += letter_count[i] / total * (letter_count[i] - 1) / (total - 1)
        prob[i] = letter_count[i] / total
        koinc2 += prob[i] ** 2
    return koinc1, koinc2


def get_occurrence_indexes(text: str, list_of_substr: set, remove_unpaired: bool = True) -> dict:
    result_dict = {}
    for substr in list_of_substr:
        subst_occurrances = []
        substr_index = -1
        while True:
            substr_index = text.find(substr, substr_index + 1)
            if substr_index == -1:
                break
            subst_occurrances.append(substr_index)
        result_dict[substr] = subst_occurrances
    if remove_unpaired:
        return {k: v for k, v in result_dict.items() if len(v) > 1}

    return result_dict


def get_occurrence_distances(occurrence_indexes: dict) -> dict:
    result_dict = {}
    for key, value in occurrence_indexes.items():
        len_val = len(value)
        res = [value[j] - value[i] for i in range(len_val) for j in range(i + 1, len_val)]
        result_dict[key] = res
    return result_dict


def calculate_frequency_of_factors(distance_dict: dict, distance_as_set: bool = True) -> dict:
    calculated_factors_dict = {}
    unique_distances = set().union(*[value for _, value in distance_dict.items()])
    unique_factors = set()
    result_frequency_dict = {}
    for unique_dis in unique_distances:
        number_factors = KMat.factors(unique_dis)
        calculated_factors_dict[unique_dis] = number_factors
        unique_factors.update(number_factors)

    for key in unique_factors:
        result_frequency_dict[key] = 0

    for key, dist_list in distance_dict.items():
        for distance in dist_list:
            for prime in calculated_factors_dict[distance]:
                result_frequency_dict[prime] += 1

    return result_frequency_dict


def get_diff_of_probabilities(
        template_freq_dict: dict,
        cipher_freq_dict: dict,
        alphabet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') -> dict:
    result_dict = {}
    # alphabet_size = len(alphabet)
    # template_sorted = [(k, template_freq_dict[k]) for k in sorted(template_freq_dict, key=template_freq_dict.get, reverse=True)]
    # column_sorted = [(k, cipher_freq_dict[k]) for k in sorted(cipher_freq_dict, key=cipher_freq_dict.get, reverse=True)]
    # min_length = min(len(column_sorted), len(template_sorted))
    # for letter in alphabet:
    #     sum = 0
    #     letter_dec = KTrans.ctoi(letter)
    #     for i in range(min_length):
    #         sum += pow((template_sorted[i][1] - column_sorted[(i + letter_dec) % min_length][1]), 2)
    #     result_dict[letter] = sum
    for letter in alphabet:
        sum = 0
        letter_dec = KTrans.ctoi(letter)
        for t_letter, t_prob in template_freq_dict.items():
            transformed_letter = KTrans.itoc((KTrans.ctoi(t_letter) + letter_dec) % 26)
            if transformed_letter in cipher_freq_dict:
                sum += pow(t_prob - cipher_freq_dict[transformed_letter], 2)
        # for t_letter, t_prob in KU.get_bottom_n_from_dict(template_freq_dict, 6):
        #     transformed_letter = KTrans.itoc((KTrans.ctoi(t_letter) + letter_dec) % 26)
        #     if transformed_letter in cipher_freq_dict:
        #         sum += pow(t_prob - cipher_freq_dict[transformed_letter], 2)
        result_dict[letter] = sum
    return result_dict


def get_sum_of_prob_diff_in_columns_and_template(template_text_prob: dict, list_of_prob_in_columns: list) -> list:
    result_list = []
    for column_prob_dict in list_of_prob_in_columns:
        result_list.append(get_diff_of_probabilities(template_text_prob, column_prob_dict))
    return result_list


def get_n_least_valued_for_each_column(list_of_letter_prob_in_column: list, bottom_n: int) -> list:
    result_list = []
    for letter_prob_in_column_dict in list_of_letter_prob_in_column:
        column_least_probable = []
        for k, v in KU.get_bottom_n_from_dict(letter_prob_in_column_dict, bottom_n):
            column_least_probable.append((k, v))
        result_list.append(column_least_probable)
    return result_list


def get_password_combinations_dict(list_of_expected_letters_in_column: list) -> dict:
    combinations = it.product(*[letter_list for letter_list in list_of_expected_letters_in_column])
    result_dict = {}
    for specific_comb in combinations:
        password = ''
        probability = 0
        for letter, letter_prob in specific_comb:
            password += letter
            probability += letter_prob
        result_dict[password] = probability
    return result_dict


def get_probable_password_length(encrypted_text: str, factor_frequency: dict, coinc_threshold: float = 0.038) -> list:
    possible_length_list = []
    for length, count in KU.most_rated(factor_frequency):
        lists_of_text = KTrans.split_text_to_n_texts(encrypted_text, length)
        is_possible_length = True
        for column_text in lists_of_text:
            if coincidence(column_text)[0] < coinc_threshold:
                is_possible_length = False
                break
        if is_possible_length:
            possible_length_list.append(length)
    return possible_length_list
