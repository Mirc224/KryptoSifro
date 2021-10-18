def getk1Inv(k1: int, alphabetSize:int):
    for i in range(1,alphabetSize-1):
        if (i * k1) % alphabetSize == 1:
            return i
    return 0

def getk2Inv(k1inv: int, k2: int, alphabetSize: int):
    return (getk1Inv(k1inv, alphabetSize) * (alphabetSize - k2)) % alphabetSize

def ctoi(ch: chr):
    if(ord(ch) >= ord('A') and ord(ch) <= ord('Z')):
        return ord(ch) - ord('A')
    if (ord(ch) >= ord('a') and ord(ch) <= ord('z')):
        return ord(ch) - ord('a')
    return 26


def itoc(i: int):
    if i == 26:
        return ' '
    else:
        return chr(i + ord('A'))

def encrypt(text: str, k1: int, k2: int, alphabetSize: int):
    cyphredText = []
    for ch in text:
        cyphredChar = (ctoi(ch) * k1 + k2) % alphabetSize
        cyphredText.append(cyphredChar)
    return cyphredText

def decrypt(textArray: list, k1: int, k2: int, alphabetSize: int):
    result = []
    for num in textArray:
        result.append((getk1Inv(k1, alphabetSize) * num + getk2Inv(k1, k2, alphabetSize)) % alphabetSize)
    return result

def translateText(textArray: list):
    result = ''
    for i in textArray:
        result += itoc(i)
    return result

def getCypherFromEncryptedText(text: str):
    result = []
    for ch in text:
        result.append(ctoi(ch))
    return result


if __name__ == '__main__':
    #sifra = encrypt("TOTO JE TAJNA SPRAVA", 5, 15, 27)
    #print(translateText(sifra))
    textToCrack = 'LIYGTOGDPOAUPDFQNVPVDAQV'
    sifra = getCypherFromEncryptedText(textToCrack)
    alphabetSize = 27
    for i in range(2, alphabetSize):
        if i % 2 == 0 or i % 3 == 0:
            continue
        for j in range(0, alphabetSize):
            desifrovane = decrypt(sifra, i, j, alphabetSize)
            print('{0} {1}: '.format(i,j) + translateText(desifrovane))

    # desifrovane = decrypt(getCypherFromEncryptedText('CECEKGIKCPG PKYJTPMP'), 5, 15, 27)
    # print(getk1Inv(5, 27))
    # print(getk2Inv(5, 15, 27))
    # print(translateText(desifrovane))
