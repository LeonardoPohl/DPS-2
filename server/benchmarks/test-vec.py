import sys

sys.path.append("..")

import logging
logging.basicConfig(level=logging.DEBUG)

import numpy as np

from distributed_execution import DistributedExecution
from time import time

SIZE = 1024
VECTOR_COUNT = 100000
REPETITIONS = 10
CPU_OVERHEAD = 1

if __name__ == "__main__":
    for _ in range(REPETITIONS):
        A = np.random.random((SIZE, SIZE))

        def vector_multiplication(v: np.ndarray) -> np.ndarray:
            a = np.dot(A, v)
            for j in range(CPU_OVERHEAD):
                a = np.dot(A, a)
            return a

        vectors = [np.random.random(SIZE) for _ in range(VECTOR_COUNT)]
        start = time()
    
        with DistributedExecution(packages=["numpy"], timeout_in_seconds=5) as d:
            results = d.map(vector_multiplication, vectors, chunk_size=2)

        end = time()
        print(end - start)
