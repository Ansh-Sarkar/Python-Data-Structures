def radixSort(arr, placevalue):
    countArr = [0] * 10
    inputsize = len(arr)

    for i in range(inputsize):
        placeElt = (arr[i] // placevalue) % 10
        countArr[placeElt] += 1

    for i in range(1, 10):
        countArr[i] += countArr[i-1]

    outputArr = [0] * inputsize
    i = inputsize - 1
    while i >= 0:
        currentElt = arr[i]
        placeElt = (arr[i] // placevalue) % 10
        countArr[placeElt] -= 1
        new_pos = countArr[placeElt]
        outputArr[new_pos] = currentElt
        i -= 1

    return outputArr

def rad_sort(arr):
    max_elt = max(arr)

    D = 1
    while max_elt > 0:
        max_elt /= 10
        D += 1

    placeVal = 1

    outputArr = arr
    while D > 0:
        outputArr = radixSort(outputArr, placeVal)
        placeVal *= 10
        D -= 1

    return outputArr

arr = [62,22,5,85,10,10,55,55]
print(arr)
sorted = rad_sort(arr)
print(sorted)