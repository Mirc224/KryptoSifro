from KryptoUtils import General as KU


def decrypt(textArray: list, p: int, c: int, alphabetSize: int):
    for k1inv in KU.range_without_factors(alphabetSize):
        k2inv = (p - c * k1inv) % alphabetSize
        result = getDecryptedList(textArray, k1inv, k2inv, alphabetSize)
        print(f'{str(k1inv).ljust(10)}{str(k2inv).ljust(10)}{KU.DecASCIIToText(result).ljust(10)}')

def getDecryptedList(numberArray: list, k1inv: int, k2inv: int, alphabetSize: int):
    result = []
    for num in numberArray:
        result.append((k1inv * num + k2inv) % alphabetSize)
    return result

def crack(cryptedFile: str, etalonFile: str, alphabetSize: int):
    template_frequency_table = KU.freqAnalyzeToProb(
        KU.clear_text(
            KU.textToTelegraphAlphabet(
                KU.readFile(etalonFile)), '[0123()-.,/]'))
    crypted_text = KU.readFile(cryptedFile)
    crypted_frequency_table = KU.freqAnalyzeToProb(crypted_text)
    crypted_text_DecASCII = KU.textToDecASCII(crypted_text)
    print(crypted_text)
    print(crypted_text_DecASCII)
    print()
    print('{}{}{}'.format('k1_inv'.ljust(10), 'k2_inv'.ljust(10), 'result'.ljust(10)))
    for orig, val in KU.mostFrequent(template_frequency_table):
        orig_ctoi = KU.ctoi(orig)
        for cryp, val2 in KU.mostFrequent(crypted_frequency_table):
            decrypt(crypted_text_DecASCII, orig_ctoi, KU.ctoi(cryp), alphabetSize)
