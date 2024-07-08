import random as r

x = 20
random_number = r.randint(1, x) 
guessed_number = 0

while random_number != guessed_number:
    guessed_number = int(input(f"Guess a number between [1 to {x}]:  "))
    if guessed_number > random_number:
        print("Choose a smaller number!")

    elif guessed_number < random_number:
        print("Choose a larger number!")

    else:
        print(f"Yeah!! you guessed it right!")



print(f"The number is {random_number}")