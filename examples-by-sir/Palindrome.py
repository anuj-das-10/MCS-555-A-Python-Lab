def is_palin(s):
    if len(s) <= 1:
        return True

    return s[0] == s[-1] and is_palin(s[1:-1])



string = input("Enter a string: ").lower()

# Condition for Alphanumeric value detection!
isAlphaNum = False
nums = [str(x) for x in range(0, 10)]
for c in string:
    if c in nums: 
        isAlphaNum = True
        print("Please provide a string without numeric values!")
        break

if not isAlphaNum:
    if is_palin(string):
        print(f"'{string}' is a palindrome string.")
    else:
        print(f"'{string}' is not a palindrome string.")