def fibonacci(n):
    if n <= 1:
        return 0
    elif n == 2: 
        return 1
    else: 
        return fibonacci(n-1) + fibonacci(n-2)
    
series = []
terms = int(input("Enter the number of terms:  "))

for i in range(1, terms + 1):
    series.append(fibonacci(i))

print(f"Fibonacci Series:  {series}")