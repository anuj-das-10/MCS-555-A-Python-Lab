def power(x, n):
    result = 1
    for i in range(1, n + 1):
        result *= x
    return result

print(power(2, 3))