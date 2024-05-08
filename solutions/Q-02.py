def GCD(m, n):
    if m < n:
        m, n = n, m
    while m % n != 0:
        m, n = n, m % n
    return n


m = 10
n = 15
print(f"The GCD of {m} and {n} is {GCD(m, n)}")