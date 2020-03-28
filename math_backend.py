import sympy
import secrets
import math
#import random

def luo_alkuluvut(*, bittimäärä=512):
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
        #voidaan myös valita 65537 (bitteinä yksi ykkönen ja muut nollia)
        satunnaisluku = secrets.randbits(len(fii.to_bytes(int(512/4), byteorder="big")))
        satunnaisluku = sympy.prevprime(satunnaisluku)
        # gcd = Euclidean algorithm
        val = math.gcd(satunnaisluku, fii)
        if val == 1:
            valittu = satunnaisluku
            return valittu



def valitse_d(e, fii):
    # Extended Euclidean algorithm
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = fii

    while e > 0:
        temp1 = temp_fii // e
        temp2 = temp_fii - temp1 * e
        temp_fii = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_fii == 1:
        return d + fii


if __name__ == "__main__":
    alkuluvut = luo_alkuluvut()
    print("alkuluvut: ", alkuluvut)
    fii = (alkuluvut[0] - 1) * (alkuluvut[1] - 1)
    e = valitse_e(fii)
    d = valitse_d(e, fii)
    print("e: ", e)
    print("d:", d)
    print(len("225791077739873387007868366109268087721"))