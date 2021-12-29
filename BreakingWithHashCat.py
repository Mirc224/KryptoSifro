import base64

# shadow_files_list = [
#     "./SifrovaneTexty/shadow1.txt",
#     "./SifrovaneTexty/shadow2.txt",
#     "./SifrovaneTexty/shadow3.txt",
#     "./SifrovaneTexty/shadow4.txt",
# ]
# shadow_cont = []
# for file_name in shadow_files_list:
#     with open(file_name, 'r') as f:
#         shadow_cont.extend(f.readlines())
#
# def uprav(x: str):
#     x = x.rstrip()
#     tmp = x.split(':')
#     return tmp[2] + ":" + tmp[1]
#
#
# result = list(map(uprav, shadow_cont))
# with open('./SifrovaneTexty/shadow_hash.txt', 'w+') as f:
#     f.write('\n'.join(result))

# name_file = 'Slovniky/zenske_mena.txt'
# final_dict = 'Slovniky/finalZenskeMena.txt'
# names = []
# with open(name_file, mode='r', encoding='utf-8') as f:
#     names = f.readlines()
#
# names = list(map(lambda x: x.strip(), names))
# with open(final_dict, "w", encoding='utf-8') as f:
#     f.write('\n'.join(names))
#     f.write('\n')
# print("Mena zapisane")
#
# names = list(map(lambda x: unidecode.unidecode(x.lower()), names))
# with open(final_dict, "a", encoding='utf-8') as f:
#     f.write('\n'.join(names))
#     f.write('\n')
# print("Mena bez diakritiky")
#
# def zdrobni_muz1(x: str):
#     res = x + "ko"
#     return res
#
# def zdrobni_muz2(x: str):
#     res = x[:3] + "ko"
#     return res
#
# def zdrobni_muz3(x: str):
#     res = x[:2] + "ko"
#     return res
#
#
# def zdrobni_zena1(x: str):
#     res = x[:-1] + "ka"
#     return res
#
# def zdrobni_zena2(x: str):
#     res = x[:3] + "ka"
#     return res
#
# def zdrobni_zena3(x: str):
#     res = x[:2] + "ka"
#     return res
#
# def zdrobni_zena4(x: str):
#     res = x[:3] + "inka"
#     return res
#
# def zdrobni_zena5(x: str):
#     res = x[:3] + "icka"
#     return res
#
# names_vanila = names
#
# names_ko1 = list(map(zdrobni_zena1, names_vanila))
# names_ko2 = list(map(zdrobni_zena2, names_vanila))
# names_ko3 = list(map(zdrobni_zena3, names_vanila))
# names_ko4 = list(map(zdrobni_zena4, names_vanila))
# names_ko5 = list(map(zdrobni_zena5, names_vanila))
#
#
# names = names_vanila + names_ko1 + names_ko2 + names_ko3 + names_ko4 + names_ko5
# names_upper = []
#
# for name in names:
#     for i in range(len(name)):
#         names_upper.append(name[:i] + name[i:].capitalize())
#
# with open(final_dict, "a", encoding='utf-8') as f:
#     f.write('\n'.join(names_upper))
#     f.write('\n')
# print("Mena s jednym zapisane velkym")


# lower_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# upper_a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# pswd = []
#
# all_alphnum = lower_a + upper_a + num
#
#
# for r in [7]:
#     pswd = []
#     for s in itertools.product(lower_a, repeat=r):
#         if len(pswd) > 200000:
#             with open(final_dict, "a", encoding='utf-8') as f:
#                 f.write('\n'.join(pswd))
#             pswd = []
#         pswd.append(''.join(s))
#     with open(final_dict, "a", encoding='utf-8') as f:
#         f.write('\n'.join(pswd))
#     print(f"{r} male kombinacie zapisane")
#
#
# pswd =[]
# for r in [4,5]:
#     pswd = []
#     for s in itertools.product(all_alphnum, repeat=r):
#         pswd.append(''.join(s))
#         if len(pswd) > 500000:
#             with open(final_dict, "a", encoding='utf-8') as f:
#                 f.write('\n'.join(pswd))
#             pswd = []
#     with open(final_dict, "a", encoding='utf-8') as f:
#         f.write('\n'.join(pswd))
#     print(f"{r} velke kombinacie zapisane")


# shadow_files_list = [
#     "./SifrovaneTexty/shadow1.txt",
#     "./SifrovaneTexty/shadow2.txt",
#     "./SifrovaneTexty/shadow3.txt",
#     "./SifrovaneTexty/shadow4.txt",
# ]
# shadow_cont = []
# for file_name in shadow_files_list:
#     with open(file_name, 'r') as f:
#         shadow_cont.extend(f.readlines())
#
# def uprav(x: str):
#     x = x.rstrip()
#     tmp = x.split(':')
#     return tmp[2] + ":" + tmp[1]
#
#
# result = list(map(uprav, shadow_cont))
# with open('./SifrovaneTexty/shadow_hash.txt', 'w+') as f:
#     f.write('\n'.join(result))
from hashlib import md5
from base64 import b64encode


def crypt(passwd, salt):
    m = md5()
    m.update(passwd.encode('utf-8'))
    m.update(salt.encode('utf-8'))
    # b64encode(m.digest())
    return [m.digest(), b64encode(m.digest()), m.hexdigest()]

# shadow_files_list = [
#     "./SifrovaneTexty/shadow1.txt",
#     "./SifrovaneTexty/shadow2.txt",
#     "./SifrovaneTexty/shadow3.txt",
#     "./SifrovaneTexty/shadow4.txt",
# ]
# shadow_cont = []
# for file_name in shadow_files_list:
#     with open(file_name, 'r') as f:
#         shadow_cont.extend(f.readlines())
#
# def uprav(x: str):
#     x = x.rstrip()
#     tmp = x.split(':')
#     base64_bytes = tmp[2].encode('ascii')
#     message_bytes = base64.b64decode(base64_bytes)
#     res = message_bytes.hex()
#     return tmp[0] + ":" + res + ":" + tmp[1]
# #
# # #
# hash_file = './SifrovaneTexty/shadow_hash_wu.txt'
# result = list(map(uprav, shadow_cont))
# with open(hash_file, 'w+') as f:
#     f.write('\n'.join(result))
#
# hashcat_cracked_file = 'C:/Users/miros/Downloads/hashcat-6.2.5/hashcat-6.2.5/hashcat.potfile'
# cracked_hashes = []
# with open(hashcat_cracked_file, 'r') as f:
#     cracked_hashes = f.readlines()
# cracked_hashes = list(map(lambda x: x.rstrip(), cracked_hashes))
# print(cracked_hashes)
#
# hashes_wu = './SifrovaneTexty/hashesRemaining.txt'
# hashes_with_names = []
# with open(hashes_wu, 'r') as f:
#     hashes_with_names = f.readlines()
#
# hashes_with_names = list(map(lambda x: x.rstrip(), hashes_with_names))
#
# solved = []
# for cracked in cracked_hashes:
#     cradked_split = cracked.split(':')
#     for i, hashed in enumerate(hashes_with_names):
#         hashed_split = hashed.split(':')
#         if cradked_split[0] == hashed_split[1]:
#             solved.append(':'.join([str((i//100)+1), hashed_split[0], cracked]))
#
# solvedHashes_file = './SifrovaneTexty/solvedHashes.txt'
# solved.sort(key=lambda x: x[0])
# with open(solvedHashes_file, 'w+') as f:
#     f.write('\n'.join(solved))


# res = crypt('heslo', '02SK64Xv')
# print(res)
# base_message = res[1].decode('utf-8')
# base64_bytes = base_message.encode('ascii')
# message_bytes = base64.b64decode(base64_bytes)
# print(message_bytes.hex())

