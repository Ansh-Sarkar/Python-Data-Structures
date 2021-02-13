def fib(n):
    assert n>=0 and int(n)==n , 'The number should be a positive integer'
    if n in [0,1]:
        return n
    else:
        return fib(n-1)+fib(n-2)
