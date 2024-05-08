def factors(n):
    allfactors = []
    for i in range(1, n + 1):
        if n % i == 0:
            allfactors.append(i)
    return allfactors

def isPrime(n):
    return (factors(n) == [1, n])

def firstNPrime(n):
    count, i, primes = 0, 1, []
    while count < n:
        if isPrime(i):
            count, primes = count + 1, primes + [i]
        i += 1
    return primes

n = int(input("Enter the value of n:  "))
print(f"List of first {n} prime numbers:  {firstNPrime(n)}")