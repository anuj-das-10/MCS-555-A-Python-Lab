# Write a python program to check if file exists or not.

file_name = input("Enter the file name:  ")

try:
    file = open(file_name, "x")
    print(f"{file_name} has been created successfully!")
    file.close()

except FileExistsError:
    print("File already exists!")
