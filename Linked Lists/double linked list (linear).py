# defining the node class
class Node:
    def __inti__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

#DLL = Double Linked List

# defining the double linked list class
class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "DLL created successfully !"

    # Inserting a node in the Doubly linked list 
    # Time Complexity : O(n) , Space Complexity : O(1)
    def insertNode(self, nodeValue, location):
        if self.head is None:
            print("The node cannot be inserted")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == 1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode

    # traversing in doubly linked list , same as in the
    # case of singly linked list\
    # Time Complexity : O(n) , Space Complexity : O(1)
    def traverseDLL(self):
        if self.head is None:
            print("The DLL DNE")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                
    # traversing in doubly linked list in the reverse 
    # direction 
    # Time Complexity : O(n) , Space Complexity : O(1)
    def reverseTraverseDLL(self):
        if self.head is None:
            print("The DLL DNE")
        else:
            tempNode=self.tail
            while tempNode:
                print(tempNode.value)
                tempNode=tempNode.prev
                
    # search function for a doubly linked list (DLL)
    # Time Complexity : O(n) , Space Complexity : O(1)
    def searchDLL(self,nodeValue):
        if self.head is None:
            return "The DLL DNE"
        else:
            tempNode=self.head
            while tempNode:
                if tempNode.value==nodeValue:
                    return tempNode.value
                tempNode=tempNode.next
            return "The value was not found in the DLL"
        
    # creating a function to delete a node from a given 
    # doubly linked list
    # if you pass a negative location value , it deletes 
    # the 2nd node .....
    # Time Complexity : O(n) , Space Complexity : O(1)
    def deleteNode(self,location):
        if self.head is None:
            print("The DLL DNE")
        else:
            if location==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.head.prev=None
            elif location==1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.tail=self.tail.prev
                    self.tail.next=None
            else:
                curNode=self.head
                index=0
                while index<location-1:
                    curNode=curNode.next
                    index+=1
                curNode.next=curNode.next.next
                curNode.next.prev=curNode
            print("The node has been successfully deleted")
    
    # function to delete the entire DLL
    # Time Complexity : O(n) , Space Complexity : O(1)
    def delDLL(self):
        if self.head is None:
            print("The DLL DNE")
        else:
            tempNode=self.head
            while tempNode:
                tempNode.prev=None
                tempNode=tempNode.next
            self.head=None
            self.tail=None
            print("The DLL has been successfully deleted")
            
                
                    
        
    
            
                
