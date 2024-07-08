# Write a python program to read contents line by line from a external file. 

filename = "test.txt"

# Reading Line by Line (Methods - 1)
file = open(filename, "r")
for line in file:
    print(line, end="")
file.close()


# Reading Line by Line (Methods - 2)
file = open(filename, "r")
lines = file.readlines()
print(f"\n\n{lines}\n\n")

for line in lines:
    print(line, end="")

file.close()


