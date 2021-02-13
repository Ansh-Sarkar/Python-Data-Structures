class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        
class SLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
            
    def insertSSL(self,value,location):
        newNode=Node(value)
        if self.head==None:
            self.head=newNode
            self.tail=newNode
        else:
            if location==0:
                newNode.next=self.head
                self.head=newNode
            elif location==1:
                newNode.next=None
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=newNode
                newNode.next=nextNode
    
    def traverseSLL(self):
        if self.head==None:
            print("The SLL DNE")
        else:
            node=self.head
            while node is not None:
                print(node.value)
                node=node.next
                
    def searchSLL(self,nodeValue):
        if self.head is None:
            return "The SLL DNE"
        else:
            node=self.head
            while node is not None:
                if node.value==nodeValue:
                    return nodeValue
                node=node.next
            return "The value DNE in the SLL"
        
    def deleteNodeSLL(self,location):
        if self.head==None:
            print("The SLL DNE")
        else:
            if location==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
            elif location==1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    node=self.head
                    while node is not None:
                        if node.next==self.tail:
                            break
                        node=node.next
                    node.next=None
                    self.tail=None
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=nextNode.next
                
    def deleteEntireSLL(self):
        if self.head==None:
            print("The SLL DNE")
        else:
            self.head=None
            self.tail=None
                
# main driver code
sll=SLinkedList()
sll.insertSSL(1,1)
sll.insertSSL(2,1)
sll.insertSSL(3,1)
sll.insertSSL(4,1)
sll.insertSSL(5,1)
sll.insertSSL(6,1)
print([node.value for node in sll])
