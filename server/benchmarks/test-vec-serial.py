import logging

import numpy as np
from tqdm import tqdm

import pandas as pd
from time import time

from constants import n_reps

SIZE = 4096
VECTOR_COUNT = 10000

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    A = np.random.random((SIZE, SIZE))
    vectors = [np.random.random(SIZE) for i in range(VECTOR_COUNT)]

    def vector_multiplication(v: np.ndarray) -> np.ndarray:
        return np.dot(A, v)

    for i in range(n_reps):
        start = time()
        results = list(tqdm(map(vector_multiplication, vectors), total=len(vectors)))
        end = time()

        df.loc[len(df.index)] = ["Vec", True, n_reps, 0, end - start, sys.argv[1]]

    df.to_csv('results.csv', mode='a', index=False)