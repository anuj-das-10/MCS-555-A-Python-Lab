"""There are four different methods (modes) for opening a file:

"r" - Read: Opens a file for reading, error if the file does not exist (Default value)
"a" - Append: Opens a file for appending, creates the file if it does not exist
"w" - Write: Opens a file for writing, creates the file if it does not exist
"x" - Create: Creates the specified file, returns an error if the file exists


In addition you can specify if the file should be handled as binary or text mode:

"t" - Text - Text mode (Default value)
"b" - Binary - Binary mode (e.g. images)

"""

# Create - It will return error if file exists!
create_file = "python_tutorial.docx"
with open(create_file, "x") as file:
    print(create_file, "has been created successfully!")


filename = "welcome.txt"
# Write
with open(filename, "w") as file:
    file.write("Hello World from ~ADX!\nWelcome to Pythonic World!")

# Read
with open(filename, "r") as file:
    text = file.read()
    print(text + "\n\n")

# Append
with open(filename, "a") as file:
    file.write("\n\nFollow github.com/anuj-das-10 and Give a Star!")



# Reading Again after Appending!
with open(filename, "rt") as file:
    text = file.read()
    print(text)