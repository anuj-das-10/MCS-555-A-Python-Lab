# 2. Write a python program to compute the sum of all elements in a 2D-Array using List Comprehension.

def calcSum(L):
    sum_of_items = 0
    for item in L:
        sum_of_items += item
    return sum_of_items

nums = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

total_sum = calcSum([calcSum(List) for List in nums])

print(f"The sum of all the elements of 2D-Array is {total_sum}")