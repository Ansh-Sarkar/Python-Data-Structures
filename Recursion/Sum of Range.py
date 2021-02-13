def sumOfRange(num):
    if num==0:
        return 0
    else:
        return num+sumOfRange(num-1)