import logging

import numpy as np
from tqdm import tqdm

SIZE = 4096
VECTOR_COUNT = 10000

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    A = np.random.random((SIZE, SIZE))
    vectors = [np.random.random(SIZE) for i in range(VECTOR_COUNT)]

    def vector_multiplication(v: np.ndarray) -> np.ndarray:
        return np.dot(A, v)

    results = list(tqdm(map(vector_multiplication, vectors), total=len(vectors)))
