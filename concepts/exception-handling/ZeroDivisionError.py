try: 
    x = int(input("Enter first number:  "))
    y = int(input("Enter second number:  "))
    print(f"{x} / {y} = {x/y}")
    print(f"{x} * {y} = {x*y}")
    print(f"{x} + {y} = {x+y}")
    print(f"{x} - {y} = {x-y}")


except ValueError:
    print("Invalid Input!")

except ZeroDivisionError:
    print("Division by zero is not possible!")
    print(f"{x} * {y} = {x*y}")
    print(f"{x} + {y} = {x+y}")
    print(f"{x} - {y} = {x-y}")
    

except Exception as e:
    print("Error: ", e)   

else:
    print("No exception occurred!")

print("Program executed successfully after try-except block!")