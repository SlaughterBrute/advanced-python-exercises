from math import sqrt
from time import time
from functools import lru_cache

def time_it(f):
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print("Execution time:", end-start)
        return result
    return wrapper

@lru_cache
def is_divisible_by(a, b):
    return a % b == 0


def is_prime(n):
    return not any(is_divisible_by(n,i) for i in range(2, int(sqrt(n))+1))

@time_it
def primes(n):
    return [x for x in range(1, n+1) if is_prime(x)]

print(primes(100))