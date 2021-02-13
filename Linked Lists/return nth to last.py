# return the nth element from the last node
from LinkedList import LinkedList

# defining the function
# Time Complexity : O(n) , Space Complexity : O(1)
def nthToLast(ll,n):
    pointer1=ll.head
    pointer2=ll.head
    
    for i in range(n):
        if pointer2 is None:
            return None
        pointer2=pointer2.next
    
    while pointer2:
        pointer1=pointer1.next
        pointer2=pointer2.next
    return pointer1

# driver code
ll=LinkedList()
ll.generate(10,0,99)
print(ll)
print(nthToLast(ll,3))