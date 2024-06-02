message = "Welcome to Python Programming!"

with open("welcome.txt", "w") as file:
    file.write(message)

with open("welcome.txt", "r") as file:
    for line in file:
        print(line, end="")
