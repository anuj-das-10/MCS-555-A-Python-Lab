def power(x, n):
    result = 1
    for i in range(1, n + 1):
        result *= x
    return result


x = 2
n = 3
print(f"{x} to the power of {n} is {power(x, n)}")