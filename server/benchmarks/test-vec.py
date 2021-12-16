import sys

sys.path.append("..")

import logging

import numpy as np

from distributed_execution import DistributedExecution
from time import time

SIZE = 4096
VECTOR_COUNT = 10000
REPETITIONS = 10

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    for _ in range(REPETITIONS):
        A = np.random.random((SIZE, SIZE))

        def vector_multiplication(v: np.ndarray) -> np.ndarray:
            return np.dot(A, v)

        vectors = [np.random.random(SIZE) for _ in range(VECTOR_COUNT)]
        correct_results = list(map(vector_multiplication, vectors))
        start = time()
        with DistributedExecution(packages=["numpy"]) as d:
            results = d.map(vector_multiplication, vectors, chunk_size=2)
        end = time()
        print(end - start)
