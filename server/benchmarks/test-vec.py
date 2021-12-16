import sys

sys.path.append("..")

import logging

import numpy as np

from distributed_execution import DistributedExecution
from constants import n_reps, rmse
from time import time

SIZE = 4096
VECTOR_COUNT = 10000

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    for i in range(n_reps):
        A = np.random.random((SIZE, SIZE))
        def vector_multiplication(v: np.ndarray) -> np.ndarray:
            return np.dot(A, v)

        vectors = [np.random.random(SIZE) for _ in range(VECTOR_COUNT)]
        correct_results = list(map(vector_multiplication, vectors))
        
        for i in range(n_reps):
            start = time()
            with DistributedExecution(packages=["numpy"]) as d:
                results = d.map(vector_multiplication, vectors, chunk_size=2)
            end = time()
            print(end - start)
            rmserr = rmse(correct_results, results)
            print(rmserr)
