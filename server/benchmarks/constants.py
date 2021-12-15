import numpy as np

n_reps = 10

columns = ["Experiment", "Sequential", "Repetition", "RMSE", "Execution Time", "Number of Clients"]

def rmse(actual, pred): 
    actual, pred = np.array(actual), np.array(pred)
    return np.sqrt(np.square(np.subtract(actual,pred)).mean())


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

def vector_multiplication(v: np.ndarray) -> np.ndarray:
  return np.dot(A, v)