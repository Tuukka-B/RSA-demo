import sympy
import random
from math import gcd

def createprimes():
    minrange = 10 * 10 ** 1
    maxrange = 10 * 10 ** 2
    primenum = []
    for x in range(0, 2):
        chosen = random.randint(minrange, maxrange)
        primenum.append(sympy.prime(chosen))
    return primenum

def choose_e(num):
    chosen = 0
    x = 1
    while True:
        ri = random.randint(x, num)
        val = gcd(ri, num)
        if val == 1:
            chosen = ri
            return chosen





if __name__ == "__main__":
    primes = createprimes()
    print("primes: ", primes)
    num = choose_e(160)
    print("e: ", num)