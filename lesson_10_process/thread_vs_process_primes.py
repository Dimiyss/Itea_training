import math
import time
import concurrent.futures as cf
import os

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]


def is_prime(n):
    if n % 2 == 0:
        return False

    sq = int(math.floor(math.sqrt(n)))
    for i in range(3, sq + 1, 2):
        if n % i == 0:
            return False

    return True


if __name__ == '__main__':

    start = time.time()
    for prime in PRIMES:
        print(f'{prime} is prime? {is_prime(prime)}')
    print(f'Time one thread = {time.time() - start}')


    start = time.time()
    with cf.ThreadPoolExecutor(max_workers=10) as ex:
        for num, prime in zip(PRIMES, ex.map(is_prime, PRIMES)):
            print(f'{num} is prime? {prime}')
    print(f'Time 10 threads = {time.time() - start}')

    start = time.time()
    with cf.ProcessPoolExecutor(max_workers=10) as ex:
        for num, prime in zip(PRIMES, ex.map(is_prime, PRIMES)):
            print(f'{num} is prime? {prime}')
    print(f'Time 10 threads = {time.time() - start}')

