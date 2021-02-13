def nestedEvenSum(obj,sum_=0):
    for key in obj:
        if type(obj[key]) is dict:
            sum_+=nestedEvenSum(obj[key])
        elif type(obj[key]) is int and obj[key]%2==0:
            sum_+=obj[key]
    return sum_
