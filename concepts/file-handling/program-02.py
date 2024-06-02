# Write a python program to take input from a file "input.txt" and write the content to another file "output.txt".

input_file = open("input.txt", "r")
output_file = open("output.txt", "w")

contents = input_file.read()
output_file.write(contents)

input_file.close()
output_file.close()