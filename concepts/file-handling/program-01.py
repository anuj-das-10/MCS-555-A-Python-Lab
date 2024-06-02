# Write a python program to read contents line by line from a external file. 

file = open("test.txt", "r")

for line in file:
    print(line, end="")

file.close()