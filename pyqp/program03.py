# 3. Write a python function to find all the factors of the number.

def factors(n):
  ff = []
  for i in range(1, n+1):
    if n % i == 0:
      ff.append(i)
  return ff

fact = factors(10)
print(fact)