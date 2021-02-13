class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        
class CSLL:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
            if node==self.tail.next:
                break
            
    def createCSLL(self,nodeValue):
        node=Node(nodeValue)
        node.next=node
        self.head=node
        self.tail=node
        return "The CSLL has been created"
    
    def insertCSLL(self,value,location):
        if self.head is None:
            return "The head reference is None"
        else:
            newNode=Node(value)
            if location==0:
                newNode.next=self.head
                self.head=newNode
                self.tail.next=newNode
            elif location==1:
                newNode.next=self.tail.next
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
            return "The node has been successfully inserted"
        
    def traverseCSLL(self):
        if self.head is None:
            print("CSLL DNE")
        else:
            tempNode=self.head
            while tempNode:
                print(tempNode.value)
                tempNode=tempNode.next
                if tempNode==self.tail.next:
                    break
                
    def searchCSLL(self,nodeValue):
        if self.head is None:
            return "CSLL DNE"
        else:
            tempNode=self.head
            while tempNode:
                if tempNode.value==nodeValue:
                    return tempNode.value
                tempNode=tempNode.next
                if tempNode==self.tail.next:
                    return "Node DNE in CSLL"
                
    def deleteCSLL(self,location):
        if self.head is None:
            print("CSLL DNE")
        else:
            if location==0:
                if self.head==self.tail:
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.tail.next=self.head
            elif location==1:
                if self.head==self.tail:
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    node=self.head
                    while node:
                        if node.next==self.tail:
                            break
                        node=node.next
                    node.next=self.head
                    self.tail=node
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=nextNode.next
                
    def deleteEntireCSLL(self):
        self.head=None
        self.tail.next=None
        self.tail=None
                    
        