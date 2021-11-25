from time import time

def nth_prime(x):
  n = 5000000
  prime = [True for i in range(n + 1)]
  
  p = 2
  while (p * p <= n):
          
      # If prime[p] is not changed,
      # then it is a prime
      if (prime[p] == True):
              
          # Update all multiples of p
          for i in range(p * p, n + 1, p):
              prime[i] = False
                
      p += 1
  
  primes = []
  for p in range(2, n + 1):
      if prime[p]:
          primes.append(p)
  
  return primes[x]

def Example():
  # Build Data
  
  l = [i for i in range(100)]

  start_seq = time()
  seq_map = list(map(nth_prime, l))
  end_seq = time()

  print(f"Sequential map time: {end_seq-start_seq}, solution: {seq_map}")  
