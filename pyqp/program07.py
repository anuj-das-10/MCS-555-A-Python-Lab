""" 7. Consider a tuple definition given below:

        test = ((1, 'a'), (3, 'b'), (2, 'a'), (7, 'b'))

    Write a function that returns a tuple which contains 
    the min, max number in test and also unique words in test.
"""

def process(data):
    nums = [num for num, _ in data]
    words = {word for _, word in data}
    return (min(nums), max(nums), words)

test = ((1, 'a'), (3, 'b'), (2, 'a'), (7, 'b'))
print(f"Result: {process(test)}")