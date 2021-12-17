import logging
from time import time

import numpy as np
import pandas as pd
from constants import columns, n_reps
from tqdm import tqdm

SIZE = 4096
VECTOR_COUNT = 10000

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    A = np.random.random((SIZE, SIZE))
    vectors = [np.random.random(SIZE) for i in range(VECTOR_COUNT)]

    df = pd.DataFrame(columns=columns)

    def vector_multiplication(v: np.ndarray) -> np.ndarray:
        return np.dot(A, v)

    for i in range(n_reps):
        start = time()
        results = list(tqdm(map(vector_multiplication, vectors), total=len(vectors)))
        end = time()

        df.loc[len(df.index)] = ["Vec", True, end - start, 0]

    df.to_csv("results.csv", mode="a", index=False)
import pandas as pd
from constants import columns, n_reps
from tqdm import tqdm

from time import time
import numpy as np
import pandas as pd

SIZE = 1024
VECTOR_COUNT = 1000

if __name__ == "__main__":
    df = pd.DataFrame(columns=columns)

    for _ in range(n_reps):        
        A = np.random.random((SIZE, SIZE))

        def vector_multiplication(v: np.ndarray) -> np.ndarray:
            return np.dot(A, v)

        vectors = [np.random.random(SIZE) for _ in range(VECTOR_COUNT)]
        start = time()

        results = list(tqdm(map(vector_multiplication, vectors), total=len(vectors)))

        end = time()
        print(end - start)

        df.loc[len(df.index)] = ["Vec", True, end - start, 0, 0]

    df.to_csv("results.csv", mode="a", index=False, header=False)
