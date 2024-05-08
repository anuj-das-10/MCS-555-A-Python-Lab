def factors(n):
    allfactors = []
    for i in range(1, n + 1):
        if n % i == 0:
            allfactors.append(i)
    return allfactors

def isPrime(n):
    return (factors(n) == [1, n])


x = int(input("Enter a number:  "))

if isPrime(x):
    print(f"{x} is a prime number!")
else:
    print(f"{x} is not a prime number!")