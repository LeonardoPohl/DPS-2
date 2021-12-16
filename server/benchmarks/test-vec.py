import sys

sys.path.append("..")

import logging

import numpy as np

from distributed_execution import DistributedExecution
from constants import n_reps, rmse, vector_multiplication
import pandas as pd
from time import time

SIZE = 4096
VECTOR_COUNT = 10000

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    A = np.random.random((SIZE, SIZE))
    vectors = [np.random.random(SIZE) for i in range(VECTOR_COUNT)]
    corr_res = list(map(vector_multiplication, vectors), total=len(vectors))
    
    for i in range(n_reps):
        start = time()
        with DistributedExecution(packages=["numpy"]) as d:
            results = d.map(vector_multiplication, vectors, chunk_size=2)
        end = time()
        rmserr = rmse(corr_res, results)
        
        df.loc[len(df.index)] = ["Vec", False, n_reps, rmserr, end - start, sys.argv[1]]

    df.to_csv('results.csv', mode='a', index=False)