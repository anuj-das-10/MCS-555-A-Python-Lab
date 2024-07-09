def get_total(*numbers):
    total = 0     # It has a local scope that means it can be accessed outside the class
    
    for num in numbers:
        total += num
    
    return total

# print(total)    # It will give error
nums = (12, 34, 45, 65, 77)
result = get_total(*nums)
print(f"Sum of all the elements in {nums} is {result}")