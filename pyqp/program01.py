# 1. Write a python program to convert numbers from octal, binary and hexadeciaml system to decimal number system.

print(bin(5))
print(oct(5))
print(hex(5))

def binary_to_decimal():
    binary = input("Enter a binary number: ")
    decimal = int(binary, 2)
    print(f"Binary {binary} in decimal is {decimal}")
    

def octal_to_decimal():
    octal = input("Enter an octal number: ")
    decimal = int(octal, 8)
    print(f"Octal {octal} in decimal is {decimal}")


def hexadecimal_to_decimal():
    hexdec = input("Enter a hexadecimal number: ")
    decimal = int(hexdec, 16)
    print(f"Hexadecimal {hexdec} in decimal is {decimal}")



binary_to_decimal()
octal_to_decimal()
hexadecimal_to_decimal()
