def isPalindrome(string):
    if len(string)==0:
        return True
    if string[0]!=string[len(string)-1]:
        return False
    return isPalindrome(string[1:-1])