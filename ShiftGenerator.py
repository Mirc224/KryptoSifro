import numpy as np
from KryptoUtils import KryptoMath as KM

class ShiftGenerator:

    def __init__(self, pa_c: str, pa_z: str, pa_b: int):
        self.c = int(pa_c, 2)
        self.z = int(pa_z, 2)
        self.b = pa_b

    def next(self):
        result = self.z & 1
        newbit = bin((self.z & self.c)).count("1") % 2
        self.z = (self.z >> 1) | (newbit << (self.b - 1))
        return result

# gen = ShiftGenerator("10010001","10010000",8)
# for i in range(20):
#     generated = gen.next()
#     print(f"{i + 3}", ('{:0'+str(gen.b)+'b}').format(gen.x), generated)

# 1110010011001111
plain = "1110010011001111"
tmp = plain
result = []
while len(tmp) > 8:
    tmp_list = list(map(int, tmp[:8]))
    tmp_list.reverse()
    result.append(tmp_list)
    tmp = tmp[1:]

tmp = list(map(int, plain[:8]))
tmp.reverse()
first_z = np.array(tmp)
z_matrix = np.array(result)
# print(z_matrix)
z_inverse = KM.get_inverse_mod_matrix(z_matrix, 2)
# print(z_matrix)
# print(z_inverse)
print(np.mod(np.matmul(z_inverse, z_matrix), 2))
c_result = np.matmul(z_inverse, first_z)
# print(z_inverse, first_z, c_result)
z_or = np.mod(np.matmul(z_matrix, c_result),2)

skuska_c = np.array(list(map(int, "{:0b}".format(145))))
# print("{:0b}".format(145))

print(np.mod(np.matmul(z_matrix, skuska_c),2))
exit()
povodne_z = plain[:8]
povodne_z = povodne_z[::-1]
povodne_c = list(map(str, map(int, c_result)))
# povodne_c.reverse()
povodne_c = ''.join(povodne_c)


gen = ShiftGenerator("{:0b}".format(145), povodne_z, 8)
res = []
for i in range(16):
    res.append(str(gen.next()))
tmp = ''.join(res)
print(tmp)
# print("{:0b}".format(145))
# for c in range(256):
#     res = []
#     gen = ShiftGenerator("{:08b}".format(c), povodne_z, 8)
#     for i in range(16):
#         res.append(str(gen.next()))
#     tmp = ''.join(res)
#     if tmp == plain:
#         print(c)
