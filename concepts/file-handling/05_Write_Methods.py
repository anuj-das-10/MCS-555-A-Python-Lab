info = """STUDENTS INFO
ADX001, Anuj Das, Male.
ADX002, Pragati Dey, Female.
ADX003, Raj Patel, Male.
ADX004, Priya Singh, Female.
ADX005, Vikas Rao, Male.
ADX006, Neha Gupta, Female.
"""

with open("python.txt", "w") as file:
    file.writelines(info)

with open("python.txt", "r") as file:
    for line in file:
        print(line, end="")