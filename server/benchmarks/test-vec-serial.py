import logging

import numpy as np
from tqdm import tqdm

from time import time

from constants import n_reps

SIZE = 4096
VECTOR_COUNT = 10000

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    for i in range(n_reps):
        A = np.random.random((SIZE, SIZE))
        def vector_multiplication(v: np.ndarray) -> np.ndarray:
            return np.dot(A, v)

        vectors = [np.random.random(SIZE) for _ in range(VECTOR_COUNT)]

        start = time()
        results = list(tqdm(map(vector_multiplication, vectors), total=len(vectors)))
        end = time()
        print(end - start)
