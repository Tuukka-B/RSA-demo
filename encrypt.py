import math_backend

primes = math_backend.createprimes()
n = primes[0] * primes[1]
e_factor = (primes[0] -1)* (primes[1] -1)
e = math_backend_gcd(e_factor)
d =