# 11. Write an iterator class for printing out n ** 2 for a maximum of 5 times 
#     (n and max are the data attribute of the iterator class).


class Squares:
    def __init__(self, n, max):
        self.count = 0
        self.n = n
        self.max = max

    def __iter__(self): return self

    def __next__(self):
        if self.count >= self.max:
            raise StopIteration
        else:
            result = self.n ** 2
            self.n += 1
            self.count += 1
        return result

square = Squares(3, 5)

for num in square:
    print(num, end = ", ")