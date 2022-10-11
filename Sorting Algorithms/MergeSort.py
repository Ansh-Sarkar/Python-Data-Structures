# MergeSort in Python
def mergeSort(Arr):
    if len(Arr) > 1:

        mid = len(Arr)//2
        L = Arr[:mid]
        M = Arr[mid:]

        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                Arr[k] = L[i]
                i += 1
            else:
                Arr[k] = M[j]
                j += 1
            k += 1
            
        while i < len(L):
            Arr[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            Arr[k] = M[j]
            j += 1
            k += 1


# Print the array
def printList(Arr):
    for i in range(len(Arr)):
        print(Arr[i], end=" ")
    print()


# Driver program
if __name__ == '__main__':
    Arr = [450, 3, 68, 3250, 89, 17]

    mergeSort(Arr)

    print("Sorted array is: ")
    printList(Arr)
