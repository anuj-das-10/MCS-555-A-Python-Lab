def cube(x):
    return x*x*x

def square(x):
    return x*x

def modifyList(fx, L):
    modified_list = []
    for i in L:
        modified_list.append(fx(i))
    return modified_list


nums = [4, 6, 8, 3]
print(nums)
print(modifyList(square, nums))
print(modifyList(cube, nums))