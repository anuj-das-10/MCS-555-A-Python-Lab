# 9. Write a python program using list comprehension for the 
#    Pythagorean Theorem with triplets x, y, z below 100 and no duplicates.


def get_pythagorean_triplets(n):
    triplets = [(x, y, z) 
                for x in range(1, n)
                    for y in range(x, n)
                        for z in range(y, n)
                            if x**2 + y**2 == z**2
                ]
    return triplets


triplets = get_pythagorean_triplets(100)
print(triplets)



