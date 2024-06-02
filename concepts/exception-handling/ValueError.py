try: 
    num = int(input("Enter a number:  "))
    for i in range(1, 11):
        print(f"{num} X {i} = {num * i}")

except ValueError:
    print("Invalid Input!\nPlease provide an integer value!")