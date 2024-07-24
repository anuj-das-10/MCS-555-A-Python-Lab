# 2. Write a python function to find prime numbers upto 100.

def factors(n):
    ff = []
    for i in range(1, n+1):
        if n % i == 0:
            ff.append(i)
    return ff

def is_prime(n):
    return factors(n) == [1, n]

def prime_numbers_upto(n):
    return [i for i in range(1, n+1) if is_prime(i)]

print(prime_numbers_upto(100))