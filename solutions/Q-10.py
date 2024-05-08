# __isPalindrome__ = lambda S: True if len(S) <= 1 else S[0] == S[-1] and __isPalindrome__(S[1:-1])


def isPalindrome(string):
    string = string.lower()
    if len(string) <= 1:
        return True  
    else:
        return string[0] == string[-1] and isPalindrome(string[1:-1])
    

string = input("Enter a string:  ")

if isPalindrome(string):
    print(f"{string} is palindrome.")
else: 
    print(f"{string} is not palindrome.")