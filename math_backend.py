import sympy
import random
from math import gcd

def createprimes():
    minrange = 10 * 10 ** 2
    maxrange = 10 * 10 ** 5
    primes = []
    for x in range(0, 2):
       # primes.append(sympy. (random.randint(minrange, maxrange)))
        if primes[x] == primes[x-1]:
            primes.pop(-1)
            x = x-1

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
    num = choose_e(160)
    print(num)