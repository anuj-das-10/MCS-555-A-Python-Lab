# Global scope in Python

sum = 0   # Global variable

def addValues(*args):
    print(args)
    for value in args:
        global sum      # Modifying global variable
        sum += value

addValues(10, 12, 23, 24, 55)
print(f"Global variable:  sum = {sum}")

def add(x, y):
  # 'sum' is a local variable of add() function it will not modify the global 'sum'.
  sum = x + y
  return sum

print(add(10, 20))                      # This will modify the global variable 'sum'.
print(f"Global variable:  sum = {sum}")


