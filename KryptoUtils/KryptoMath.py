import math
from functools import reduce
import numpy as np
from numpy.linalg import linalg


def prime_factors(n: int) -> list:
    result = []
    while n % 2 == 0:
        result.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            result.append(i)
            n = n // i
    if n > 2:
        result.append(n)
    return result


def factors(n: int, remove_one: bool = True) -> set:
    result_set = set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))
    if remove_one:
        result_set.remove(1)
    return result_set


def find_factors(number: int) -> list:
    result = list()
    i = 2
    while i <= math.sqrt(number):
        if number % i == 0:
            if number / i == i:
                result.append(i)
            else:
                result.append(i)
                result.append(number//i)
        i += 1
    return result


def get_inverse_mod_matrix(matrix: np.array, modulo: int = 26) -> np.array:
    mat_det = linalg.det(matrix)
    corrective_det = pow(round(mat_det), -1, modulo)
    return np.mod(np.mod(np.rint(linalg.inv(matrix) * mat_det), modulo) * corrective_det, modulo)