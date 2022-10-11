MINIMUM = 32
  
def find_minrun(n): 
  
    r = 0
    while n >= MINIMUM: 
        r |= n & 1
        n >>= 1
    return n + r 
  
def insertion_sort(array, left, right): 
    for i in range(left+1,right+1):
        elem = array[i]
        j = i - 1
        while elem < array[j] and j>=left :
            array[j+1] = array[j]
            j -= 1
        array[j+1] = elem
    return array
              
def merge(array, l, m, r): 
  
    array_len1= m - l + 1
    array_len2 = r - m 
    left = []
    right = []
    for i in range(0, array_len1): 
        left.append(array[l + i]) 
    for i in range(0, array_len2): 
        right.append(array[m + 1 + i]) 
  
    i, j, k = 0, 0, l
   
    while j < array_len2 and  i < array_len1: 
        if left[i] <= right[j]: 
            array[k] = left[i] 
            i += 1
  
        else: 
            array[k] = right[j] 
            j += 1
  
        k += 1
  
    while i < array_len1: 
        array[k] = left[i] 
        k += 1
        i += 1
  
    while j < array_len2: 
        array[k] = right[j] 
        k += 1
        j += 1
  
def tim_sort(array): 
    n = len(array) 
    minrun = find_minrun(n) 
  
    for start in range(0, n, minrun): 
        end = min(start + minrun - 1, n - 1) 
        insertion_sort(array, start, end) 
   
    size = minrun 
    while size < n: 
  
        for left in range(0, n, 2 * size): 
  
            mid = min(n - 1, left + size - 1) 
            right = min((left + 2 * size - 1), (n - 1)) 
            merge(array, left, mid, right) 
  
        size = 2 * size 
  
  
  
  
array = [-1, 5, 0, -3, 11, 9, -2, 7, 0] 
  
print("Array:") 
print(array) 
  
tim_sort(array) 
  
print("Sorted Array:") 
print(array)
