import gmpy2
import random


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


if __name__ == "__main__":
    createprimes()