# 2. Write a python program to find GCD(or HCF) and LCD(or LCM).

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)


m = 15
n = 20

res_gcd = gcd(m, n)
print(f"The GCD of {m} and {n} is {res_gcd}.")

res_lcm = lcm(m, n)
print(f"The LCM of {m} and {n} is {res_lcm}.")
