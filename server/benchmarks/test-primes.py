import sys

sys.path.append("..")

import logging

from distributed_execution import DistributedExecution
from constants import n_reps, nth_prime, rmse
import pandas as pd

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    corr_res = list(map(nth_prime, numbers), total=len(numbers))
    
    numbers = list(range(1000))
    
    for i in range(n_reps):

        start = time()

        with DistributedExecution() as d:
            results = d.map(nth_prime, numbers, chunk_size=1)

        end = time()

        mserr = rmse(corr_res, results)
