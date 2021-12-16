import sys

sys.path.append("..")

import logging

from distributed_execution import DistributedExecution
from constants import n_reps, nth_prime, rmse
import pandas as pd
from time import time

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    numbers = list(range(100))

    corr_res = list(map(nth_prime, numbers))

    for i in range(n_reps):

        start = time()

        with DistributedExecution() as d:
            results = d.map(nth_prime, numbers, chunk_size=1)

        end = time()

        rmserr = rmse(corr_res, results)

        df.loc[len(df.index)] = ["Primes", False, n_reps, rmserr, end - start, sys.argv[1]]

    df.to_csv('results.csv', mode='a', index=False)
