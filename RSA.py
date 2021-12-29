
from random import randrange
from pip._vendor.msgpack.fallback import xrange
import primefac
# Vysledky
# n:13169004533  e:65537  y:6029832903  p:130027  q:101279  d:72739001  x:1234567890
# n:1690428486610429  e:65537  y:22496913456008  p:47816809  q:35352181  d:1308297747522113  x:1234567890
# n:56341958081545199783  e:65537  y:17014716723435111315  p:6940440583  q:8117922401  d:10931906232715055873  x:1234567890
# n:6120215756887394998931731  e:65537  y:5077587957348826939798388  p:2924446284457  q:2092777627483  d:4628379897502241593077665  x:1234567890
# n:514261067785300163931552303017  e:65537  y:357341101854457993054768343508  p:848976880459061  q:605742134588197  d:138834873007999909396179588113  x:1234567890
# n:21259593755515403367535773703117421  e:65537  y:18829051270422357250395121195166553  p:175824717389116441  q:120913567052497781  d:16561767538761904020317771857821473  x:1234567890
# n:1371108864054663830856429909460283182291  e:65537  y:35962927026249687666434209737424754460  p:29857785889724643173  q:45921317445260458967  d:836678299148177608382742375124935850305  x:1234567890

def is_prime(p, k=10):
    if p == 2 or p == 3:
        return True
    if not p & 1:
        return False

    def check(a, s, d, p):
        x = pow(a, d, p)
        if x == 1:
            return True
        for i in xrange(s - 1):
            if x == p - 1:
                return True
            x = pow(x, 2, p)
        return x == p - 1

    s = 0
    d = p - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in xrange(k):
        a = randrange(2, p - 1)
        if not check(a, s, d, p):
            return False
    return True


def generate_primes(upper_bound):
    res_file = './Resources/primes.txt'
    open(res_file, 'w').close()
    result = []
    for i in range(2, upper_bound):
        if is_prime(i,10):
            result.append(i)
        if len(result) != 0 and len(result) % 25 == 0:
            with open(res_file, 'a') as f:
                res = '\n'.join(map(str, result)) +'\n'
                f.write(res)
                result = []
    with open(res_file, 'a') as f:
        f.writelines('\n'.join(map(str,result)))


def egcd(a, b):
    u0, u1, v0, v1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        u0, u1 = u1, u0 - q * u1
        v0, v1 = v1, v0 - q * v1
    return a, u0, v0


def mod_inverse(a, n):
    gcd, u, v = egcd(a, n)
    if gcd == 1:
        return u % n


def factorize(n):
    result = []
    i = 2
    while n > 1:
        j = 0
        while n % i == 0:
            n = n / i
            j = j + 1
        if j > 0:
            result.append((i,j))
        i = i + 1
    return result


def custom_factorize(n):
    # return 29857785889724643173, 45921317445260458967
    return primefac.primefac(n)
    # val1, val2 = dict_factorize(n)
    # if val1 is not None:
    #     return val1, val2
    # print('Prime not found in precalculated primes')
    prime = primes[-1]
    # while True:
    #     prime += 2
    #     if is_prime(prime):
    #         if n % prime == 0:
    #             return (prime, 1), (n // prime, 1)

def crack(n, e, factorize):
    p, q = factorize(n)
    fi_n = (p - 1) * (q - 1)
    d = mod_inverse(e, fi_n)
    return p, q, d

def dict_factorize(n):
    for prime in primes:
        if n % prime == 0:
            return (prime, 1), (n//prime, 1)
    return None, None

res = []

n_list = [13169004533,
    1690428486610429,
    56341958081545199783,
    6120215756887394998931731,
    514261067785300163931552303017,
    21259593755515403367535773703117421,
    1371108864054663830856429909460283182291]
e = 65537
y_list = [6029832903,
22496913456008,
17014716723435111315,
5077587957348826939798388,
357341101854457993054768343508,
18829051270422357250395121195166553,
35962927026249687666434209737424754460]

# for i, n in enumerate(n_list):
#     p, q, d = crack(n, e, dict_factorize)
#     xx = pow(y_list[i], d, n)
#     print(f'p:{p}  q:{q}  d:{d}  x:{xx}')

for i in range(len(n_list)):
    p, q, d = crack(n_list[i], e, custom_factorize)
    xx = pow(y_list[i], d, n_list[i])
    print(f'n:{n_list[i]}  e:{e}  y:{y_list[i]}  p:{p}  q:{q}  d:{d}  x:{xx}')
# for i in range(len(n_list)):
#     p, q, d = crack(n_list[i], e, custom_factorize)
#     xx = pow(y_list[i], d, n_list[i])
#     print(f'n:{n_list[i]}  e:{e}  y:{y_list[i]}  p:{p}  q:{q}  d:{d}  x:{xx}')

# 1. p:101279  q:130027  d:72739001  x:1234567890
# 2. p:35352181  q:47816809  d:1308297747522113  x:1234567890

# with open('SifrovaneTexty/sprava_RSA.enc', "rb") as f:
#     while (bytes := f.read(2)):
#         out = int.from_bytes(bytes, byteorder="little")
#         inp = pow(out, d, n)
#         res.append(((inp).to_bytes(2, "little")).decode('iso-8859-2'))
#
# print(''.join(res))


