from LinkedList import LinkedList

# defining the function for partitioning the linked list 
# around a given value
# Time Complexity : O(n) , Space Complexity : O(1)
def partition(ll,x):
    curNode=ll.head
    ll.tail=curNode
    
    while curNode:
        nextNode=curNode.next
        curNode.next=None
        if curNode.value<x:
            curNode.next=ll.head
            ll.head=curNode
        else:
            ll.tail.next=curNode
            ll.tail=curNode
        curNode=nextNode
    
    if ll.tail.next is not None:
        ll.tail.next=None
        
# main driver program / code
ll=LinkedList()
ll.generate(10,0,99)
print(ll)
partition(ll,50)
print(ll)