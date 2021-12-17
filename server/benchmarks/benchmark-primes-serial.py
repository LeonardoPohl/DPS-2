import logging
from time import time

import pandas as pd
from constants import columns, n_reps
from tqdm import tqdm

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

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

    numbers = list(range(1000))
    for i in range(n_reps):
        start = time()

        results = list(tqdm(map(nth_prime, numbers), total=len(numbers)))

        end = time()
        df.loc[len(df.index)] = ["Primes", True, end - start, 0, 0]

    df.to_csv("results.csv", mode="a", index=False, header=False)
