import sympy
import random
from math import gcd

def createprimes():
    minrange = 10 * 10 ** 1
    maxrange = 10 * 10 ** 2
    primes = []
    chosen = random.randint(minrange, maxrange)
    primes.append(sympy.prime(chosen))
    chosen = random.randint(minrange, maxrange)
    primes.append(sympy.prime(chosen))
    return primes

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