info = ["Hello everyone!\n", "How are you doing?\n", "Follow me on github!"]

with open("python.txt", "w") as file:
    file.writelines(info)

with open("python.txt", "r") as file:
    for line in file:
        print(line, end="")