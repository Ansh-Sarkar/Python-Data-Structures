def flatten(arr):
    resultArr=[]
    for item in arr:
        if type(item) is list:
            resultArr.extend(flatten(item))
        else:
            resultArr.append(item)
    return resultArr