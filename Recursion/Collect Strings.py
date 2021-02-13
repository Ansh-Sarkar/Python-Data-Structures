def collectStrings(obj):
    resultArr=[]
    for key in obj:
        if type(obj[key]) is str:
            resultArr.append(obj[key])
        if type(obj[key]) is dict:
            resultArr+=collectStrings(obj[key])
    return resultArr