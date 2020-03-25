import sympy
import secrets
import math
#import random

def luo_alkuluvut(*, bittimäärä=2048):
    alkuluvut = []
    while len(alkuluvut) < 2:
        luku1 = secrets.randbits(bittimäärä)
        luku2 = secrets.randbits(bittimäärä)
        # valittu = random.randint(min_jarjestysluku, max_jarjestysluku)
        if luku1 > luku2:
            alkuluvut.append(sympy.randprime(luku2, luku1))
        else:
            alkuluvut.append(sympy.randprime(luku1, luku2))

    return alkuluvut

def valitse_e(fii):
    valittu = 0
    x = 1
    while True:
        satunnaisluku = secrets.randbelow(fii)
        val = math.gcd(satunnaisluku, fii)
        if val == 1:
            valittu = satunnaisluku
            return valittu

def valitse_d(e):
    math.fmod()



if __name__ == "__main__":
    alkuluvut = luo_alkuluvut()
    print("alkuluvut: ", alkuluvut)
    e = valitse_e(160)
    print("e: ", e)
    print(12345%2345)