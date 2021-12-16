import sys
import logging
from tqdm import tqdm
import pandas as pd
from time import time
from constants import nth_prime, n_reps, columns


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    df = pd.DataFrame(columns=columns)

    numbers = list(range(1000))
    for i in range(n_reps):    
        start = time()

        results = list(tqdm(map(nth_prime, numbers), total=len(numbers)))

        end = time()
        df.loc[len(df.index)] = ["Primes", True, n_reps, 0, end - start, 0]

    df.to_csv('results.csv', mode='a', index=False)
    # print(results)
