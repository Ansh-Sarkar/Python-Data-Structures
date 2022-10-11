'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def partition(array, low, high):
 
    
    pivot = array[high]
 
   
    i = low - 1
 
   
    for j in range(low, high):
        if array[j] <= pivot:
 
           
            i = i + 1
 
           
            (array[i], array[j]) = (array[j], array[i])
 
   
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    
    return i + 1
 

 
 
def quickSort(array, low, high):
    if low < high:
 
        pi = partition(array, low, high)
 
    
        quickSort(array, low, pi - 1)
 
        
        quickSort(array, pi + 1, high)
 
 
data = [74,205,-19,32,-94,23,378,878,297,296,795,774,771]
print("Initial Array")
print(data)
 
size = len(data)
 
quickSort(data, 0, size - 1)
 
print('Resultant Array:')
print(data)

