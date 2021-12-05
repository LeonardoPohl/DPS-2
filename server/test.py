from distributed_execution import DistributedExecution
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    def square(v: int) -> int:
        return v * v

    values = list(range(1, 101))

    with DistributedExecution() as d:
        results = d.map(square, values)

    print(results)
