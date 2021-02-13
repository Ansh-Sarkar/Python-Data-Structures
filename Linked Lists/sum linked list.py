from LinkedList import LinkedList

# function for adding the two linkedlists
# Time Complexity : O(n) , Space Complexity : O(n)
def sumList(lla,llb):
    tempa=lla.head
    tempb=llb.head
    carry=0
    ll=LinkedList()
    
    while tempa or tempb:
        result=carry
        if tempa:
            result+=tempa.value
            tempa=tempa.next
        if tempb:
            result+=tempb.value
            tempb=tempb.next
        ll.add(int(result%10))
        carry=result/10
        
    return ll

# main driver code
lla=LinkedList()
lla.generate(3,0,9)
llb=LinkedList()
llb.generate(3,0,9)
print(lla)
print(llb)
print(sumList(lla,llb))