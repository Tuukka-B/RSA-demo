import sympy
import crypto
from pycryptodome import random
from math import gcd

def luo_alkuluvut():
    min_jarjestysluku = 10 * 10 ** 1
    max_jarjestysluku = 10 * 10 ** 2
    alkuluvut = []
    for numero in range(0, 2):
        # valittu = random.random.randint(min_jarjestysluku, max_jarjestysluku)
        valittu = random.randint(min_jarjestysluku, max_jarjestysluku)
        alkuluvut.append(sympy.prime(valittu))
    return alkuluvut

def valitse_e(fii):
    valittu = 0
    x = 1
    while True:
        satunnaisluku = random.randint(x, fii)
        val = gcd(satunnaisluku, fii)
        if val == 1:
            valittu = satunnaisluku
            return valittu





if __name__ == "__main__":
    primes = createprimes()
    print("primes: ", primes)
    num = choose_e(160)
    print("e: ", num)