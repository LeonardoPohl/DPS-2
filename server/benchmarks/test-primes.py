import sys

sys.path.append("..")

import logging

from distributed_execution import DistributedExecution


def nth_prime(x):
    n = 5000000
    prime = [True for i in range(n + 1)]

    p = 2
    while p * p <= n:
        # If prime[p] is not changed,
        # then it is a prime
        if prime[p] == True:

            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False

        p += 1

    primes = []
    for p in range(2, n + 1):
        if prime[p]:
            primes.append(p)

    return primes[x]


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    numbers = list(range(1000))

    with DistributedExecution() as d:
        results = d.map(nth_prime, numbers, chunk_size=1)

    print(results)
