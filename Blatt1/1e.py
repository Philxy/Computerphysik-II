# 1 e
import numpy as np

# Prüft ob ein integer > 0 eine Primzahl ist mit dem Sieb des Eratosthenes
def isPrime(p):
    if p == 1 or p == 2: 
        return True

    upper_limit = int(p/2) + 1 # Oberes Limit an Zahlen die es zu prüfen gilt
    checked_primes = np.full(upper_limit, False,  dtype= bool) # boolean array speichert bereits gestrichene Primzahlen 
    
    for i in range(2, upper_limit):
        if not checked_primes[i-1]:
            if p % i == 0:
                return False
            else:
                for j in range(i-1, upper_limit, i):
                    checked_primes[j] = True 
    return True
    
  
# Gebe  die ersten N Primzahlen aus.
N = 100
prime_numbers = []
for i in np.arange(1,N,1):
    if isPrime(i):
        prime_numbers.append(i)
print(prime_numbers)



# Anstatt jede Zahl einzeln zu prüfen können Primzahlen auch deutlich effizienter direkt berechnet werden:


# Findet mit dem Sieb des Eratosthenes die ersten N Primzahlen und gibt diese als Liste aus. 
def get_Primes(N):
    upper_limit = int(N/2) # Obere grenze an Zahlen die es zu durchlaufen gilt
    checked_primes = np.full(upper_limit*2, False,  dtype= bool) # boolean array speichert bereits ausgeschlossene Zahlen 
    primes = []
    for i in range(2, upper_limit):
        if not checked_primes[i-1]:
            for j in range(i+i-1, upper_limit*2, i):
                checked_primes[j] = True 
    for i in range(len(checked_primes)):
        if not checked_primes[i]:
            primes.append(i+1)
    return primes


N = 100
print(get_Primes(N))