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

def valitse_d(e, fii):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi / e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi



if __name__ == "__main__":
    alkuluvut = luo_alkuluvut()
    print("alkuluvut: ", alkuluvut)
    e = valitse_e(160)
    print("e: ", e)
    print(12345%2345)