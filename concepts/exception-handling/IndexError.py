try:
    nums = [2, 3, 5, 8]
    i = int(input("Enter an index:  "))
    print(nums[i])

except IndexError:
    print("Index out of range!")