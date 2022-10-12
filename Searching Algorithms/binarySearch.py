# Searching an element returns the index of that number in the array.

def binary_search(arr, n):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low<=high:
        mid = (low + high)//2
        if arr[mid] < n:
            low = mid + 1
        elif arr[mid] > n:
            high = mid - 1
        else:
            return mid
    return -1

arr = [4, 7, 9, 16, 20, 25]
n = 7
r = binary_search(arr, n)
if r != -1:
    print(str(r))
else:
    print("Not found")
