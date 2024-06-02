# Reading File Contents

# Method - 1
"""
1. Automatic Cleanup: The file is automatically closed at the end of the with block, 
   so you do not need to explicitly call file.close(). This makes the code cleaner and more reliable.
2. Exception Safety: If an error occurs while reading the file, the file will still be closed properly.
"""
with open("python.txt", "r") as file:
    contents = file.read()
    print(contents)



# Method - 2
file = open("python.txt", "r")
contents = file.read()
print(contents)
file.close()



# Method - 3
file = open("python.txt")           # This will by default open file in Read Mode!
contents = file.read()
print(contents)
file.close()



# Method - 4: 
# Read specific number of characters and characters are less than the specified then it will not throw any error.
file = open("python.txt", "r")
contents = file.read(8)
print(contents)
file.close()