# 1. Write a python program using map function to cumpute the sum of all the elements in a 2D-Array.


def calcSum(L):
    sum_of_items = 0
    for item in L:
        sum_of_items += item
    return sum_of_items



nums = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

nums = list(map(calcSum, nums))
total_sum = calcSum(nums)

print(f"The sum of all the elements of 2D-Array is {total_sum}")