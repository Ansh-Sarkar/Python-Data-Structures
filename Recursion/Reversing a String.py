def reverse(string):
    if len(string)<=1:
        return string
    return string[len(string)-1]+reverse(string[0:len(string)-1])
