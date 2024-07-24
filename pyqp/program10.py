# 10. Write a generator function in python to print out the series:
#     S = 0.5, 1.0, 1.5, 2.0,.... upto the 10th number in the series.


def number_sequence(n, x = 0.5):
    count, seq = 0, x

    while count < n:
        yield seq
        seq += x
        count += 1


for i in number_sequence(10, 0.5):
    print(i, end = ",  ")