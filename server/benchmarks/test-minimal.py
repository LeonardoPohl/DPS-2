import sys
sys.path.append("..")

import logging
logging.basicConfig(level=logging.DEBUG)

import numpy as np
from distributed_execution import DistributedExecution

if __name__ == "__main__":
    result = list(map(np.square, range(5)))
    print(result)

    with DistributedExecution() as d:
        result = d.map(np.square, range(5))

    print(result)
