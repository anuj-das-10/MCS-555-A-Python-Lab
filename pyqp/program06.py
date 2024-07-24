# 6. Write a python program to find out the maximum and minimum elements in a list of elements.

def get_max(L):
    max = L[0]
    for x in L:
        if x > max: max = x
    return max


def get_min(L):
    min = L[0]
    for x in L:
        if x < min: min = x
    return min



ll = [51, 39, 13, 52, 29, 36,]
print(f"Given list:  {ll}")
print(f"Min Value in list: {get_min(ll)}")
print(f"Max Value in list: {get_max(ll)}")
