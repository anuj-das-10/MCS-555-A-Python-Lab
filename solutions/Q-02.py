def GCD(m, n):
    if m < n:
        m, n = n, m
    while m % n != 0:
        m, n = n, m % n
    return n



print(GCD(5, 15))