from itertools import combinations

import numpy as np
from numpy.linalg import linalg
from KryptoUtils import TextTransform as KTrans
from KryptoUtils import KryptoMath as KMat


def encrypt(text: str, matrix: np.array, alphabet_size: int = 26) -> str:
    matrix_size = matrix.shape[0]
    diff = (matrix_size - len(text) % matrix_size) % matrix_size
    text += 'A' * diff
    text_matrix = KTrans.text_to_matrix(text, matrix_size)
    ciphered_matrix = np.mod(np.matmul(matrix, text_matrix), alphabet_size)
    return KTrans.text_matrix_to_text(ciphered_matrix)


def decrypt(cipher_text: str, inverse_matrix: np.array, alphabet_size: int = 26):
    matrix_size = inverse_matrix.shape[0]
    diff = (matrix_size - len(cipher_text) % matrix_size) % matrix_size
    cipher_text += 'A' * diff

    text_matrix = KTrans.text_to_matrix(cipher_text, matrix_size)
    decrypted_matrix = np.rint(np.mod(np.matmul(inverse_matrix, text_matrix), alphabet_size))
    return KTrans.text_matrix_to_text(decrypted_matrix)


def get_suitable_matrix(text: str, matrix_size: int):
    diff = (matrix_size - len(text) % matrix_size) % matrix_size
    text += 'A' * diff
    text_matrix = KTrans.text_to_matrix(text, matrix_size)
    num_of_columns = text_matrix.shape[1]
    possible_combinations = list(combinations(range(0, num_of_columns), matrix_size))
    for combination in possible_combinations:
        tmp_matrix = text_matrix[:, combination]
        mat_det = round(linalg.det(tmp_matrix) % 26)
        if mat_det % 2 != 0 and mat_det % 13 != 0:
            return tmp_matrix
    return None

# BALQTGFGYNFUHVLOIVCGPRZJUTHGWOVWCWAJGWN => DRAHYJURAJPRIDDNESVECERZAMNOUMILUJEMTAA
# PCPOVZOJYEJXJLVINLJMIAVAVEUKZLERO => DRAHYJURAJUZZAMNONECHODMAMDRUHEHO
# NMUSMRFJGRWSWVKKDJKYTYTNSVMOJW => DRAHYJURAJBOLASOMHLUPAODPUSTMI
# DRAHYJURAJ
plain_text =          'DRAHYJURAJ'
known_ciphered_text = 'BALQTGFGYN'
known_ciphered_text = 'PCPOVZOJYE'
known_ciphered_text = 'NMUSMRFJGR'
matrix_size = 3

whole_ciphered_text = "BALQTGFGYNFUHVLOIVCGPRZJUTHGWOVWCWAJGWN"
whole_ciphered_text = "PCPOVZOJYEJXJLVINLJMIAVAVEUKZLERO"
whole_ciphered_text = "NMUSMRFJGRWSWVKKDJKYTYTNSVMOJW"

plain_text_matrix = get_suitable_matrix(plain_text, matrix_size)
print(round(linalg.det(plain_text_matrix) % 26))

ciphered_text_matrix = get_suitable_matrix(known_ciphered_text, matrix_size)
print(round(linalg.det(ciphered_text_matrix) % 26))

plain_inverse_matrix = KMat.get_inverse_mod_matrix(plain_text_matrix, 26)

origin_matrix = np.mod(np.matmul(ciphered_text_matrix, plain_inverse_matrix), 26)

print(origin_matrix)
print(encrypt(plain_text, origin_matrix, 26))
inverse_matrix = KMat.get_inverse_mod_matrix(origin_matrix, 26)
print(decrypt(whole_ciphered_text, inverse_matrix, 26))


