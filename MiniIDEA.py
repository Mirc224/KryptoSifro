from ast import Num
from typing import List
from KryptoUtils import TextTransform as KT

def xor(a: int, b: int) -> int:
    return (a ^ b) & int('0x0f', 16) # & int('0x0f', 16) to iste ako % 16


def add(a: int, b: int) -> int:
    return (a + b) & int('0x0f', 16)


def mul(a: int, b: int) -> int:
    temp = 0
    if a == 0:
        if b == 0:
            temp = 1
        else:
            temp = 17 - b
    else:
        if b == 0:
            temp = 17 - a
        else:
            temp = (a * b) % 17
    return 0 if temp == 16 else temp


def make_round(state: List[Num], keys: List[Num]) -> None:
    a = mul(state[0], keys[0])
    b = add(state[1], keys[1])
    c = add(state[2], keys[2])
    d = mul(state[3], keys[3])

    e = xor(a, c)
    f = xor(b, d)

    g = mul(e, keys[4])
    h = add(f, g)

    j = mul(h, keys[5])
    i = add(g, j)

    state[0] = xor(a, j)
    state[1] = xor(c, j)
    state[2] = xor(b, i)
    state[3] = xor(d, i)


def encrypt(state: List[Num], keys: List[List[Num]]) -> None:
    for i in range(2):
        make_round(state, keys[i])


def decrypt(state: List[Num], keys: List[List[Num]]) -> None:
    for i in reversed(range(2)):
        make_inv_round(state, keys[i])


def make_inv_round(state: List[Num], keys: List[Num]) -> None:
    e = xor(state[0], state[1])
    f = xor(state[2], state[3])

    g = mul(e, keys[4])
    h = add(f, g)

    j = mul(h, keys[5])
    i = add(g, j)

    a = xor(state[0], j)
    c = xor(state[1], j)
    b = xor(state[2], i)
    d = xor(state[3], i)

    state[0] = mul(a, INVKEYS[keys[0]])
    state[1] = add(b, 16 - keys[1])
    state[2] = add(c, 16 - keys[2])
    state[3] = mul(d, INVKEYS[keys[3]])


def split_bytes(byte_num: int) -> list:
    mask = int("0x0f", 16)
    state = [
        (byte_num >> 12) & mask,
        (byte_num >> 8) & mask,
        (byte_num >> 4) & mask,
        byte_num & mask
    ]
    return state

def join_bytes(state: int):
    result = []
    result.append((state[0]).to_bytes(1, byteorder='little'))
    result.append((state[1]).to_bytes(1, byteorder='little'))
    result.append((state[2]).to_bytes(1, byteorder='little'))
    result.append((state[3]).to_bytes(1, byteorder='little'))
    return result

INVKEYS = [0, 1, 9, 6, 13, 7, 3, 5, 15, 2, 12, 14, 10, 4, 11, 8]
state = [0, 0, 0, 0]
keys = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12]
]
file_name = 'SifrovaneTexty/sprava.enc'
mapper = {}

encrypted = []
plain = []
with open('SifrovaneTexty/block.txt', "rb") as f:
    while (bytes := f.read(2)):
        plain.append(int.from_bytes(bytes, byteorder="little"))

with open('SifrovaneTexty/block.enc', "rb") as f:
    while (bytes := f.read(2)):
        encrypted.append(int.from_bytes(bytes, byteorder="little"))

for i, key in enumerate(encrypted):
    mapper[key] = plain[i]

result = []
text_result = []
res = []

with open(file_name, "rb") as f:
    while (bytes := f.read(2)):
        cislo = int.from_bytes(bytes, byteorder="little")
        cislo = mapper[cislo]
        tmp = (cislo).to_bytes(2, "little")
        res.append(tmp.decode('iso-8859-2'))

print(''.join(res))
















