# 8. Write a python program to find the product of two different lists using map and lambda functions.

l1 = [4, 6, 8]
l2 = [9, 7, 5]

result = list(map(lambda x, y: x * y, l1, l2))
print(f"A = {l1} & B = {l2}")
print(f"Product of A & B is:  {result}")