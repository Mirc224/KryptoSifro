from KryptoUtils import General as KU
from KryptoUtils import TextTransform as KTrans
from KryptoUtils import TextAnalyze as KAnalyze
import re
'''
Vigenerovska šifra
==================
1. Nájdi výskyty opakujúcich sa trojíc znakov (indexy ich začiatkov)
2. Vypočítaj vzdialenosti medzi výskytmi opakujúcich sa trojíc znakov
3. Zisti najčastejších deliteľov daných vzdialeností (a ich násobky) - na zákalde čoho získame hypotézu na dĺžku hesla n
4. Testovanie hypotézy o dĺžke hesla n
    4.1 Rozdeľ zakódovaný text do stĺpcov o počte n
    4.2 Do sĺpca i vlož vždy i + n písmeno textu
    4.3 Zist početnosti výskytu písmen v každom zo stĺpcov
    4.4 Urči koincidencie pre jednotlivé stĺpce
    4.5 Ak je koincidencia v každom zo stĺpcov rovná prbiližne 0.6, je hypotéza o dĺžke hesla správna 
        ak je niekde koincidencia blízka 0.38 tak je hypotéza nesprávna.
5. Po zistení dĺžky hesla použijeme frekvenčnú analýzu na zistenie znakov hesla - najpočetnejšie znaky v stĺpci 
   by mali byť totožné s najpočetnejšími znakmi v bežných textoch (pre slovenčinu A, E, I, O...)
'''

'''
Prvý text na semestralku má 23 znakov a heslo: ISKOAJHKTRYZPEXNJHHXWQW

Druhy text ma dlzku 26 a heslo: XGAFQEGLRSTMJQFLSGPTKETPHI

Treti text ma dlzku 23 a heslo priblizne: kokvminteusweklauxbfswm

Stvrty text ma dlzku 29 a heslo je presne: ctojqkzpexpaawkanwsrbffsqureq
'''


def encrypt(text: str, password: str, alphabet_size: int) -> str:
    ascii_plain = KTrans.text_to_dec_ASCII(text)
    ascii_pass = KTrans.text_to_dec_ASCII(password)
    encrypted_text = ''
    pass_len = len(password)
    for i, value in enumerate(ascii_plain):
        encrypted_text += KU.itoc((value + ascii_pass[i % pass_len]) % alphabet_size)
    return encrypted_text


def decrypt(crypted_text: str, password: str, alphabet_size: int) -> str:
    ascii_encrypted = KTrans.text_to_dec_ASCII(crypted_text)
    ascii_pass = KTrans.text_to_dec_ASCII(password)
    pass_len = len(password)
    decrypted_text = ''
    for i, value in enumerate(ascii_encrypted):
        decrypted_text += KTrans.itoc((value - ascii_pass[i % pass_len]) % alphabet_size)
    return decrypted_text


if __name__ == '__main__':
    sj_template_text = KTrans.clear_text(KTrans.text_to_telegraph_alphabet(KU.read_file('.\Texty\\SJ_train_text3.txt')), '[^A-Z]')
    sj_template_freq = KAnalyze.freq_analyze_to_prob(sj_template_text)

    original_text = KU.read_file('SifrovaneTexty/vigenere_sem1.txt')
    encrypted_text = KTrans.clear_text(
        KTrans.text_to_telegraph_alphabet(original_text)
        , '[^A-Z]')

    print(encrypted_text)

    occurrence_dict = KAnalyze.get_occurrence_indexes(
        encrypted_text,
        KTrans.find_unique_substr_of_len(encrypted_text, 3)
    )

    occurrence_distance_dict = KAnalyze.get_occurrence_distances(occurrence_dict)
    freq_factors = KAnalyze.calculate_frequency_of_factors(occurrence_distance_dict)

    for k, v in KU.get_top_n_from_dict(freq_factors, 5):
        print(k, v)

    password_length_list = KAnalyze.get_probable_password_length(encrypted_text, freq_factors, 0.038)
    num_of_most_prob_pass = 5
    for pos_length in password_length_list:
        if not 20 <= pos_length <= 30:
            continue
        print(f"Password length: {pos_length}")
        lists_of_text = KTrans.split_text_to_n_texts(encrypted_text, pos_length)
        list_of_prob_in_columns = []
        for text in lists_of_text:
            list_of_prob_in_columns.append(KAnalyze.freq_analyze_to_prob(text))

        bottom_n = 1
        sum_of_prob_diff_in_columns_list = KAnalyze.get_sum_of_prob_diff_in_columns_and_template(sj_template_freq, list_of_prob_in_columns)
        result_list = KAnalyze.get_n_least_valued_for_each_column(sum_of_prob_diff_in_columns_list, bottom_n)

        pass_dict = KAnalyze.get_password_combinations_dict(result_list)

        print(f"{num_of_most_prob_pass} most probable passwords: ")
        for password, prob in KU.get_bottom_n_from_dict(pass_dict, num_of_most_prob_pass):

            print(password, prob)
            print('\n')
            new_password = password
            new_password = KU.manual_password_tuning('KDKBOTVYWTFNSIWRDTBPEQWSLSJOEHDIFQKPRZVKYPQOAA',
                                                     'CLANOKOODCHODEZEUMUSIAAKTIVOVATPOSLANCIBRITSKE',
                                                      len(new_password))
            decryptted = decrypt(encrypted_text, new_password.upper(), 26)
            print(encrypted_text[0: len(new_password) * 2])
            print(new_password * 2)
            print(decryptted[0: len(new_password) * 2])
            print('\n')
            decryptted = decrypt(encrypted_text, new_password.upper(), 26)
            print(KTrans.replace_original_with_decrypted(original_text, decryptted))

        print('Heslo je: ', new_password)



