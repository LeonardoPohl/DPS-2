import sys

sys.path.append("..")

import logging
logging.basicConfig(level=logging.DEBUG)

import numpy as np

from distributed_execution import DistributedExecution

SIZE = 1024
VECTOR_COUNT = 100000
REPETITIONS = 10
CPU_OVERHEAD = 1

if __name__ == "__main__":
    for _ in range(REPETITIONS):
        A = np.random.random((SIZE, SIZE))
        vectors = [np.random.random(SIZE) for i in range(VECTOR_COUNT)]

        def vector_multiplication(v: np.ndarray) -> np.ndarray:
            return np.dot(A, v)

        with DistributedExecution(packages=["numpy"]) as d:
            results = d.map(vector_multiplication, vectors, chunk_size=2)
