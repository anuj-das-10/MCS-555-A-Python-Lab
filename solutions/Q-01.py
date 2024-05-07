def factors(n):
    allfactors = []
    for i in range(1, n + 1):
        if n % i == 0:
            allfactors.append(i)
    return allfactors


x = int(input('Enter a number to find its factors:  '))
print(f"The factors of {x} are: {factors(x)}")