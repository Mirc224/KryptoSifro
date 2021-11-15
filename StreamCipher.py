import multiprocessing
import ntpath
import os

from KryptoUtils import TextTransform as KTrans
from KryptoUtils import General as KU
from KryptoUtils import TextAnalyze as KA

from multiprocessing import Pool

class NumberGenerator:

    def __init__(self, seed: int = 0):
        self.a = 84589
        self.b = 45989
        self.m = 217728
        self._seed = seed
        self._my_randx = seed
        self.setSeed(seed)

    def setSeed(self, seed: int):
        self._seed = seed
        self._my_randx = seed

    def rand(self):
        self._my_randx = (self.a * self._my_randx + self.b) % self.m;
        return float(self._my_randx / float(self.m))
        # self._my_randx = (8121 * self._my_randx + 28411) % 134456
        # return float(self._my_randx / 134456.0)

    def reset(self):
        self._my_randx = self._seed


def encrypt(text: str, password: str, alphabet_size: int) -> str:
    ascii_plain = KTrans.text_to_dec_ASCII(text)
    ascii_pass = KTrans.text_to_dec_ASCII(password)
    encrypted_text = ''
    pass_len = len(password)
    for i, value in enumerate(ascii_plain):
        encrypted_text += KTrans.itoc((value + ascii_pass[i % pass_len]) % alphabet_size)
    return encrypted_text


def decrypt(crypted_text: str, password: str, alphabet_size: int) -> str:
    ascii_encrypted = KTrans.text_to_dec_ASCII(crypted_text)
    ascii_pass = KTrans.text_to_dec_ASCII(password)
    pass_len = len(password)
    decrypted_text = []
    for i, value in enumerate(ascii_encrypted):
        decrypted_text.append(KTrans.itoc((value - ascii_pass[i % pass_len]) % alphabet_size))
    return ''.join(decrypted_text)

def generate_password(encrypted_text: str, generator: NumberGenerator, alphabet_size: int = 26)-> str:
    possible_password = []
    for i in range(len(encrypted_text)):
        possible_password.append(KTrans.itoc(int(generator.rand() * alphabet_size)))
    return ''.join(possible_password)

def crackPassword(path:str):
    base_file = ntpath.basename(os.path.splitext(path)[0])
    print(f'Cracking of {base_file} started')
    num_generator = NumberGenerator()
    original_text = KU.read_file(path)
    encrypted_text = KTrans.clear_text(
        KTrans.text_to_telegraph_alphabet(original_text)
        , '[^A-Z]')

    # num_generator.a = 8121
    # num_generator.b = 28411
    # num_generator.m = 134456

    base_filename = f'DesifrovaneTexty/{base_file}'

    for i in range(1, 100000):
        num_generator.setSeed(i)
        password = generate_password(encrypted_text, num_generator)
        decrypted_text = decrypt(encrypted_text, password, 26)
        text_coinc = KA.coincidence(decrypted_text)
        # print(text_coinc[0])
        if text_coinc[0] > 0.055:
            filename = f'{base_filename}/seed{i}.txt'
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "w") as f:
                f.write(KTrans.replace_original_with_decrypted(original_text, decrypted_text))
# Cviko heslo: 12345
# plain_text = 'TOTOJETAJNASPRAVA'
# generated_password = 'BFFHWZQKSHRNDWOXX'
# encrypted = encrypt(plain_text, generated_password, 26)
# print(encrypted)
# decrypted_text = decrypt(encrypted, generated_password, 26)
# print(decrypted_text)

if __name__ == '__main__':
    list_of_paths = [
        'text1_enc.txt',
        'text2_enc.txt',
        'text3_enc.txt',
        'text4_enc.txt'
    ]
    processes = []
    for file in list_of_paths:
        p = multiprocessing.Process(target=crackPassword, args=(f'SifrovaneTexty/{file}',))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
