import sympy
import secrets
import math
#import random

e = 0
fii = 0
alkuluvut = []
d = 0
n = 0
bitit = 0

def tuo_avaimet(e_i=None, fii_i=None, alkuluvut_i=[], d_i=None):
    global e
    global fii
    global alkuluvut
    global d
    if e_i is not None:
        e = e_i
    if fii_i is not None:
        fii = fii_i
    if len(alkuluvut_i) == 2:
        alkuluvut = alkuluvut_i
    if d_i is not None:
        d = d_i

def luo_alkuluvut(*, bittimäärä=16):
    global alkuluvut
    global fii
    global n
    global bitit
    bitit = bittimäärä
    if len(alkuluvut) == 2:
        input("Paina enter ylikirjoittaaksesi vanhat alkuluvut")
    alkuluvut = []
    while len(alkuluvut) < 2:
        luku1 = secrets.randbits(bitit)
        luku2 = secrets.randbits(bitit)
        # valittu = random.randint(min_jarjestysluku, max_jarjestysluku)
        if luku1 > luku2:
            alkuluvut.append(sympy.randprime(luku2, luku1))
        else:
            alkuluvut.append(sympy.randprime(luku1, luku2))

    p = alkuluvut[0]
    q = alkuluvut[1]
    n = p * q
    fii = (p - 1) * (q - 1)

    return alkuluvut, fii, n

def valitse_fii():
    global alkuluvut
    global fii
    fii = (alkuluvut[0] - 1) * (alkuluvut[1] - 1)


def valitse_e():
    global fii
    while True:
        #voidaan myös valita 65537 (bitteinä yksi ykkönen ja muut nollia)
        #satunnaisluku = secrets.randbits(len((fii).to_bytes(bitit, byteorder="big")))
        testi = 65538
        testibytes = len(testi.to_bytes(16, byteorder="big"))
        # input(testibytes)
        satunnaisluku = secrets.randbits(testibytes)
        satunnaisluku = sympy.prevprime(satunnaisluku)
        # gcd = Euclidean algorithm
        val = math.gcd(satunnaisluku, fii)
        if val == 1:
            global e
            e = satunnaisluku
            return e



def valitse_d(e_i=None, fii_i=None):
    # Extended Euclidean algorithm
    global e
    global fii
    d_i = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_fii = fii
    temp_e = e

    while temp_e > 0:
        temp1 = temp_fii // temp_e
        temp2 = temp_fii - temp1 * temp_e
        temp_fii = temp_e
        temp_e = temp2

        x = x2 - temp1 * x1
        y = d_i - temp1 * y1

        x2 = x1
        x1 = x
        d_i = y1
        y1 = y

    if temp_fii == 1:
        global d
        d = d_i + fii
        return d

def anna_avaimet():
    # e, n = julkinen avain
    # d, n = yksityinen avain
    return (e, n), (d, n)

def salaa(salaamaton_teksti, julkinen_avain=None):
    #Unpack the key into it's components
    global n
    global e
    avain = None
    if avain is not None:
        e, n = julkinen_avain
    avain = e
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** avain) % n for char in salaamaton_teksti]
    #Return the array of bytes
    return cipher


def pura(salattu_teksti,yksityinen_avain=None):
    #Unpack the key into its components
    global d
    global n
    if yksityinen_avain is not None:
        d, n = yksityinen_avain
    avain = d
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** avain) % n) for char in salattu_teksti]
    #Return the array of bytes as a string
    return ''.join(plain)


if __name__ == "__main__":
    alkuluvut = luo_alkuluvut()
    print("alkuluvut: ", alkuluvut[0])
    print("fii: ", fii)
    # fii = (alkuluvut[0][0] - 1) * (alkuluvut[0][1] - 1)
    e = valitse_e()
    print("Ok")
    d = valitse_d()
    print("e: ", e)
    print("d:", d)
    salattu = salaa("Onpa hauska juttu.")
    print(salattu)
    viesti = pura(salattu)
    print(viesti)