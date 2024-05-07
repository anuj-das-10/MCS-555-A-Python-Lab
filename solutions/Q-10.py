__isPalindrome__ = lambda S: True if len(S) <= 1 else S[0] == S[-1] and __isPalindrome__(S[1:-1])


def isPalindrome(string):
    if len(string) <= 1:
        return True  
    else:
        return string[0] == string[-1] and isPalindrome(string[1:-1])
    

print(__isPalindrome__("121"))
print(isPalindrome("woww"))