file_name = input("Enter file name:  ")

try:
    file = open(file_name, "x")
    print(f"{file_name} has been created successfully!")

except FileExistsError:
    print(f"{file_name} already exists!")