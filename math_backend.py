import sympy
import random
from math import gcd

def createprimes():
    minrange = 10 * 10 ** 2
    maxrange = 10 * 10 ** 5
    primes = []
    for x in range(0, 2):
        primes.append(gmpy2.next_prime(random.randint(minrange, maxrange)))
        if primes[x] == primes[x-1]:
            primes.pop(-1)
            x = x-1

    return primes

def greatestcd(num):
    greatest = 0
    for x in range(1, num):
        val = gcd(x, num)
        if val > greatest:
            greatest = val

    return greatest



if __name__ == "__main__":
    num = greatestcd(160)
    print(num)