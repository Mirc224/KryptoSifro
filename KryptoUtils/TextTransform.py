from itertools import combinations
import re

import numpy as np
import unidecode


def ctoi(ch: chr) -> int:
    if ord('A') <= ord(ch) <= ord('Z'):
        return ord(ch) - ord('A')
    if ord('a') <= ord(ch) <= ord('z'):
        return ord(ch) - ord('a')
    return 26


def itoc(i: int) -> chr:
    i = int(i)
    if i == 26:
        return ' '
    else:
        return chr(i + ord('A'))


def text_to_dec_ASCII(text: str) -> list:
    result = []
    for ch in text:
        result.append(ctoi(ch))
    return result


def text_to_telegraph_alphabet(text: str) -> str:
    return unidecode.unidecode(re.sub(' +', ' ', text.replace('\n', ' '))).upper()


def clear_text(text: str, ignoredChars: str = None) -> str:
    if ignoredChars is None:
        return re.sub(r'[^A-Z]', '', text)
    return re.sub(ignoredChars, '', text)


def dec_ASCII_to_text(numberArray: list) -> str:
    result = ''
    for i in numberArray:
        result += itoc(i)
    return result


def split_text_to_n_texts(text: str, num_of_splits: int) -> list:
    result_list = []
    for n in range(num_of_splits):
        result_list.append(''.join([text[i] for i in range(n, len(text), num_of_splits)]))
    return result_list


def ctoi_letter_only(ch: chr):
    if ord('A') <= ord(ch) <= ord('Z'):
        return ord(ch) - ord('A')
    if ord('a') <= ord(ch) <= ord('z'):
        return ord(ch) - ord('a')
    return -1


def find_unique_substr_of_len(text: str, sub_length: int) -> set:
    substr_list = [text[x: y] for x, y in combinations(range(len(text) + 1), r=2) if len(text[x:y]) == sub_length]
    return set(substr_list)


def replace_original_with_decrypted(original_text: str, decrypted_text: str) -> str:
    counter = 0
    for i in range(len(original_text)):
        if original_text[i].isalpha():
            original_text = original_text[:i] + decrypted_text[counter] + original_text[i + 1:]
            counter += 1
    return original_text


def text_to_matrix(text: str, row_size: int) -> np.array:
    return np.array(text_to_dec_ASCII(text)).reshape((-1, row_size)).transpose()


def text_matrix_to_text(text_matrix: np.array) -> str:
    return dec_ASCII_to_text(text_matrix.transpose().flatten())