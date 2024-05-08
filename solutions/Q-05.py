def factors(n):
    allfactors = []
    for i in range(1, n + 1):
        if n % i == 0:
            allfactors.append(i)
    return allfactors

def isPrime(n):
    return (factors(n) == [1, n])

def getPrimeUpto(n):
    primes = []
    for i in range(1, n + 1):
        if isPrime(i):
            primes.append(i)
    return primes


n = int(input("Enter the value of n:  "))

print(f"All the prime numbers upto {n} is:  {getPrimeUpto(n)}")