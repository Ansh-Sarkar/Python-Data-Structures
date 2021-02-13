def decimalToBinary(n):
    assert int(n)==n , 'The number should be an integer only'
    if n==0:
        return 0
    return n%2 + 10*decimalToBinary(int(n/2))