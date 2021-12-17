import logging

from tqdm import tqdm

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    def nth_prime(x):
        n = 5000000
        prime = [True for i in range(n + 1)]

        p = 2
        while p * p <= n:
            if prime[p] == True:
                for i in range(p * p, n + 1, p):
                    prime[i] = False

            p += 1

        primes = []
        for p in range(2, n + 1):
            if prime[p]:
                primes.append(p)

        return primes[x]

    numbers = list(range(100))
    results = list(tqdm(map(nth_prime, numbers), total=len(numbers)))
