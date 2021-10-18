from KryptoUtils import KryptoMath
from KryptoUtils import TextTransform
'''
Coincidence: 0.06 = monoalphabetic
Coincidence: 0.038 = polyalphabetic cyphre
'''


def range_without_factors(size: int) -> list:
    return [x for x in range(1, size) if x not in KryptoMath.find_factors(size)]


def most_rated(dictionary: dict) -> tuple:
    for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=True):
        yield k, v


def least_rated(dictionary: dict) -> tuple:
    for k, v in sorted(dictionary.items(), key=lambda item: item[1]):
        yield k, v


def read_file(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text


def get_top_n_from_dict(dictionary: dict, top_n: int) -> tuple:
    counter = 0
    for key, value in most_rated(dictionary):
        if counter < top_n:
            yield key, value
        else:
            break
        counter += 1


def get_bottom_n_from_dict(dictionary: dict, bottom_n: int):
    counter = 0
    for key, value in least_rated(dictionary):
        if counter < bottom_n:
            yield key, value
        else:
            break
        counter += 1


def manual_password_tuning(
        decrypt_text_substr: str,
        required_mapping: str,
        password_len: int,
        alphabet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') -> str:
    result = ''
    alphabet_size = len(alphabet)
    for i in range(len(required_mapping)):
        tmp1 = TextTransform.ctoi(required_mapping[i])
        tmp2 = TextTransform.ctoi(decrypt_text_substr[i])
        index = (tmp2 - tmp1) % alphabet_size
        result += alphabet[index]
    return result[0: password_len]


