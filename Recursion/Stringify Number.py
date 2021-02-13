def stringifyNumbers(obj):
    newObj=obj
    for key in newObj:
        if type(newObj[key]) is int:
            newObj[key]=str(newObj[key])
        if type(newObj[key]) is dict:
            newObj[key]=stringifyNumbers(newObj[key])
    return newObj
