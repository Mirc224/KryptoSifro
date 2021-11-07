
def feistel_f(R: int, K: int) -> int:
    output = int("0x0000",16)
    output += R
    output += K
    return output


def feistel_round(L: int, R: int, K: int):
    temp = R
    R = L ^ feistel_f(R, K)
    L = temp
    return L, R


def feistel_encrypt(L: int, R: int, K_list: list):
    for K in K_list:
        L, R = feistel_round(L, R, K)
    temp = R
    R = L
    L = temp
    return L, R

def feistel_decrypt(L: int, R: int, K_list: list):
    for K in reversed(K_list):
        L, R = feistel_round(L, R, K)
    temp = R
    R = L
    L = temp
    return L, R


L = int("0x12345678", 16)
R = int("0x90ABCDEF", 16)
K = [
    int("0x11111111", 16), int("0x22222222", 16), int("0x33333333", 16), int("0x44444444", 16),
    int("0x55555555", 16), int("0x66666666", 16), int("0x77777777", 16), int("0x88888888", 16)
]

print(f"({hex(L)}, {hex(R)})")
L, R = feistel_encrypt(L, R, K)
print(f"->({hex(L)}, {hex(R)})")
L, R = feistel_decrypt(L, R, K)
print(f"->({hex(L)}, {hex(R)})")