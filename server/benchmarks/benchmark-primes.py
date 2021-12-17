import sys

sys.path.append("..")

import logging
from time import time

import pandas as pd
from constants import columns, n_reps

from distributed_execution import DistributedExecution

CHUNK_SIZE = 1

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    numbers = list(range(1000))

    df = pd.DataFrame(columns=columns)

    def nth_prime(x):
        n = 5000000
        prime = [True for i in range(n + 1)]

        p = 2
        while p * p <= n:
            if prime[p] == True:
                for i in range(p * p, n + 1, p):
                    prime[i] = False

            p += 1

        primes = []
        for p in range(2, n + 1):
            if prime[p]:
                primes.append(p)

        return primes[x]

    for i in range(n_reps):

        start = time()

        with DistributedExecution() as d:
            results = d.map(nth_prime, numbers, chunk_size=CHUNK_SIZE)

        end = time()

        df.loc[len(df.index)] = ["Primes", False, end - start, sys.argv[1], CHUNK_SIZE]

    df.to_csv("results.csv", mode="a", index=False, header=False)
