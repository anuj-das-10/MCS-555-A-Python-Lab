# 4. Write a python function to show how functions can be passed to a function.

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def mapper(fx, L):
    for x in L:
        print(fx(x), end=" ")
    print()

mapper(square, [1, 2, 3, 4, 5])
mapper(cube, [1, 2, 3, 4, 5])