import sys

sys.path.append("..")

import logging
logging.basicConfig(level=logging.DEBUG)

import numpy as np

from distributed_execution import DistributedExecution
from time import time

SIZE = 1024
VECTOR_COUNT = 1000
CHUNK_SIZE = 5

if __name__ == "__main__":
    df = pd.DataFrame(columns=columns)
    for _ in range(n_reps):
        A = np.random.random((SIZE, SIZE))

        def vector_multiplication(v: np.ndarray) -> np.ndarray:
            return np.dot(A, v)

        vectors = [np.random.random(SIZE) for _ in range(VECTOR_COUNT)]
        start = time()
    
        with DistributedExecution(packages=["numpy"], timeout_in_seconds=500) as d:
            results = d.map(vector_multiplication, vectors, chunk_size=CHUNK_SIZE)

        end = time()
        df.loc[len(df.index)] = ["Vec", False, end - start, sys.argv[1], CHUNK_SIZE]

    df.to_csv("results.csv", mode="a", index=False, header=False)
