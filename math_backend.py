import sympy
import secrets
import math
import time

e = 0
fii = 0
alkuluvut = []
d = 0
n = 0
bitit = 0

def tuo_avaimet(e_i=None, fii_i=None, alkuluvut_i=[], d_i=None):
    # tuodaan globaalit muuttujat
    global e
    global fii
    global alkuluvut
    global d
    #korvataan globaalit muuttujat, jos parametreissa uusia arvoja
    if e_i is not None:
        e = e_i
    if fii_i is not None:
        fii = fii_i
    if len(alkuluvut_i) == 2:
        alkuluvut = alkuluvut_i
    if d_i is not None:
        d = d_i

def luo_alkuluvut_fii(*, bittimäärä=1024):
    # tuodaan globaalit muuttujat
    global alkuluvut
    global fii
    global n
    global bitit
    # määritetään bittimäärä alkuluvuille
    alkuaika = time.time()
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

        alkuluvut.append(sympy.prevprime(alkuluvut[0]))

    p = alkuluvut[0]
    q = alkuluvut[1]
    n = p * q
    loppuaika = time.time()
    fii = (p - 1) * (q - 1)
    kulunut = round((loppuaika - alkuaika) * 1000)
    print("Aikaa n:n luontiin kului:", kulunut, "millisekuntia")

    return alkuluvut, fii, n

def valitse_e(vakio_e=None):
    global fii
    while True:
        # satunnaisluku = secrets.randbits(len(fii.to_bytes(bitit//4, byteorder="big")))
        # valitaan 65537 luvuksi, jonka pohjalta eksponentti e lasketaan
        e_kanta = 32768  # = 65537 / 2
        # koska toteutuksessamme käytämme tavuja ja bittejä voimakkaasti avuksi,
        # muodostamme e:n, että se sisältää yhtä monta tavua, kuin e_kanta
        tavumaara = 0
        e_kanta_bits = 0
        satunnaisluku = 0
        if not vakio_e:
            tavumaara = int(math.log(e_kanta, 256)) + 1
            e_kanta_bits = len(e_kanta.to_bytes(tavumaara, byteorder="big")) * 8 + 4
            print("e:n koko on ", e_kanta_bits, "bittiä!")
            # muodostetaan kaksi lukua, josta haemme seuraavaksi alimman alkuluvun
            # (e:n täytyy olla aina pienempi kuin itse alkuluvut ja fii, siksi alkuluku valitaan aina pienemmäksi kuin ne)
            satunnaisluku = secrets.randbits(e_kanta_bits)
            satunnaisluku = sympy.prevprime(satunnaisluku)
        elif vakio_e > fii:
            raise ValueError("eksponentti e ei saa olla suurempi kuin fii, kokeile toisella numerolla...")
        else:
            satunnaisluku = vakio_e
            tavumaara = int(math.log(vakio_e, 256)) + 1
            e_vakio_bits = len(vakio_e.to_bytes(tavumaara, byteorder="big")) * 8
            print("e:n koko on ", e_vakio_bits, "bittiä!")


        if not sympy.isprime(satunnaisluku):
            satunnaisluku = sympy.prevprime(satunnaisluku)

        # gcd on algoritmi, joka kulkee nimellä 'Euclidean algorithm'
        # sillä varmistetaan, että e:ksi valitulla satunnaisluvulla ei ole muita yhteisiä tekijöitä fii:n kanssa, paitsi
        # numero 1.
        val = math.gcd(satunnaisluku, fii)
        while val != 1:
            satunnaisluku = sympy.nextprime(satunnaisluku)
            val = math.gcd(satunnaisluku, fii)
        global e
        e = satunnaisluku
        return e


def valitse_d(e_i=None, fii_i=None):
    # tämä algoritmi kulkee nimellä 'Extended Euclidean algorithm'
    # algoritmi etsii ehdot, jossa totetuu ax + by = gcd(a, b)
    # meillä yhtälöön sijoitetaan x(fii) + d(e) = gcd(x, d)
    global e
    global fii
    if e is None:
        raise ValueError("Virhe: e ei määritelty! Ohjelma sammuu...")
    d_i = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_fii = fii
    temp_e = e
    if e_i is not None and fii_i is not None:
        temp_fii = fii_i
        temp_e = e_i

    while temp_e > 0:
        #kolme seuraavaa riviä antavat temp_fiille saman arvon kuin gcd(temp_fii_temp_e)
        temp1 = temp_fii // temp_e
        temp2 = temp_fii - temp1 * temp_e
        temp_fii = temp_e
        temp_e = temp2

        # lasketaan d:lle ja muille muuttujille arvo ylempien laskujen pohjalta
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

def ota_avaimet(julkinen_avain, yksityinen_avain):
    global e, d, n
    e, n = julkinen_avain
    d, n = yksityinen_avain

def salaa(salaamaton_teksti, julkinen_avain=None):
    # otetaan globaalit muuttujat käyttöön
    alkuaika = time.time()
    global n
    global e
    avain = None
    # korvataan globaalit muuttujat, jos parametreissa on annettu uudet arvot avaimille
    if avain is not None:
        e, n = julkinen_avain
    if e is None:
        raise ValueError("Virhe: e ei määritelty! Ohjelma sammuu...")

    # määritetään avain ((kosmeettinen toimenpide, sillä voisimme käyttää myös suoraan muuttujaa e)
    avain = e
    #Muutetaan jokainen kirjain salatuksi numeroksi käyttämällä kaavaa a^b mod m
    salattu = [(ord(char) ** avain) % n for char in salaamaton_teksti]
    #Palautetaan salatut kirjaimet listana
    loppuaika = time.time()
    kulunut = round((loppuaika - alkuaika) * 1000)
    print("Aikaa salaukseen kului:", kulunut, "millisekuntia")
    return salattu

def pura(salattu_teksti,yksityinen_avain=None):
    # otetaan käyttöön globaalit muuuttujat
    alkuaika = time.time()
    global d
    global n

    # korvataan globaalit muuttujat jos parametreissa on annettu uudet
    if yksityinen_avain is not None:
        d, n = yksityinen_avain

    # määritetään avain (kosmeettinen toimenpide, sillä voisimme käyttää myös suoraan muuttujaa d)
    avain = d
    """
    Pow-funktio (pow(x, y, z):
    x - kantanumero
    y - eksponenttinumero
    z - modulus-numero
    """
    # Puretaan salaus avaimella käyttäen kaavaa a^b mod m
    plain = [chr(pow(char, avain, n)) for char in salattu_teksti]
    # Palautetaan purettu teksti string-muuttujana
    loppuaika = time.time()
    kulunut = round((loppuaika - alkuaika) * 1000)
    print("Aikaa purkuun kului:", kulunut, "millisekuntia")

    return ''.join(plain)


if __name__ == "__main__":

    alkuluvut = luo_alkuluvut_fii()
    print("alkuluvut: ", alkuluvut[0])
    print("n: ", alkuluvut[2])
    print("fii: ", fii)
    # pituus = int(math.log(fii, 256)) + 1
    # input(pituus)
    e = valitse_e(900000)
    d = valitse_d()
    print("e: ", e)
    print("d:", d)
    viesti = "Testailtu!"
    salattu = salaa(viesti)
    print("Salattu viesti:", salattu)
    viesti = pura(salattu)
    print("Purettu viesti:", viesti)
    """
    e = 9
    p = 71
    q = 83
    fii = (p-1)*(q-1)
    n = p * q
    tuo_avaimet(e, fii, [p, q])
    d = valitse_d()
    print("d:", d)
    salattu = salaa("d", (e, n))
    print("Salattu:", salattu)
    purettu = pura(salattu)
    print("Purettu:", purettu)
    """