# __length__ = lambda L: 0 if L == [] else 1 + __length__(L[1:])

def length(L):
    if L == []:
        return 0
    else:
        return 1 + length(L[1:])
    

mylist = ["ABC", "BCD", 1, 2, 3, 4, 5, True, 7.5] 
print(f"Given List:  {mylist}") 
print(f"The length of the given list is {length(mylist)}")