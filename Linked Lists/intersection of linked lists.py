from LinkedList import LinkedList,Node

# defining the function for finding intersection of 
# two given linkedlists
# Time Complexity : O(A+B) , A = length of linked list A
#                          , B = length of linked list B
# Space Complexity : O(1)
def intersection(lla,llb):
    if lla.tail is not llb.tail:
        return False
    lena=len(lla)
    lenb=len(llb)
    shorter=lla if lena<lenb else llb
    longer=llb if lenb>lena else lla
    
    diff=len(longer)-len(shorter)
    longerNode=longer.head
    shorterNode=shorter.head
    
    for i in range(diff):
        longerNode=longerNode.next
        
    while shorterNode is not longerNode:
        shorterNode=shorterNode.next
        longerNode=longerNode.next
        
    return longerNode

# helper addition method
def addSameNode(lla,llb,value):
    tempNode=Node(value)
    lla.tail.next=tempNode
    lla.tail=tempNode
    llb.tail.next=tempNode
    llb.tail=tempNode
    
# driver code    
lla=LinkedList()
lla.generate(3,0,10)
llb=LinkedList()
llb.generate(4,0,10)
addSameNode(lla,llb,11)
addSameNode(lla,llb,14)
print(lla)
print(llb)
print(intersection(lla,llb))
    
        