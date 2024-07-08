# read()	    Returns the file content
# readable()	Returns whether the file stream can be read or not (Boolean)
# readline()	Returns one line from the file
# readlines()	Returns a list of lines from the file

filename = "read.txt"

# Check if the file is readable or not.
file = open(filename, "r")
print(f"Is readable?  {file.readable()}")
file.close()


# Reading entire content.
file = open(filename, "r")
contents = file.read()
print(f"\n{contents}\n")
file.close()


# Reading a single Line.
file = open(filename, "r")
print(file.readline())
file.close()


# Reading Line by Line (Methods - 1)
file = open(filename, "r")
lines = file.readlines()
print(lines, end="\n\n")

for line in lines:
    print(line, end="")

file.close()


# Reading Line by Line (Methods - 2)
file = open(filename, "r")
print("\n")
for line in file:
    print(line, end="")
file.close()