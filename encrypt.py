import math_backend

alkuluvut = math_backend.luo_alkuluvut(bittimäärä=512)
n = alkuluvut[0] * alkuluvut[1]
fii = (alkuluvut[0] - 1) * (alkuluvut[1] - 1)
e = math_backend.valitse_e(fii)
d = math_backend.valitse_d(e, fii)

print("n: ", n)
print("fii: ", fii)
print("e: ", e)
print("d: ", d)