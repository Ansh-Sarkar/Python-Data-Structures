# CDLL = Circular Doubly Linked List
# The following are the function which are generally associated with a CDLL
# defining the node structure
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

# defining the class structure for the circular
# doubly linked list


class CDLL:
    def __inti__(self):
        self.head = None
        self.tail = None

    # print([node.value for node in __name_of_class_object__])
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    # function for creation of a DLL
    # Time Complexity : O(1) , Space Complexity : O(1)
    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        return "The CDLL is created successfully"

    # function for inserting a Node in the CDLL
    # Time Complexity : O(n) , Space Complexity : O(1)
    def insertNode(self, nodeValue, location):
        if self.head is None:
            return "The CDLL DNE"
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
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
            return "The Node has been successfully inserted"

    # traversal of a circular doubly linked list
    # Time Complexity : O(n) , Space Complexity : O(1)
    def traverseCDLL(self):
        if self.head is None:
            print("The CDLL DNE")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next

    # reverse traversing a CDLL
    # Time Complexity : O(n) , Space Complexity : O(1)
    def reverseTraverseCDLL(self):
        if self.head is None:
            print("The CDLL DNE")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev

    # searching function for a CDLL
    # Time Complexity : O(n) , Space Complexity : O(1)
    def searchCDLL(self, nodeValue):
        if self.head is None:
            return "The CDLL DNE"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                if tempNode == self.tail:
                    return "The element was not found in the CDLL"
                tempNode = tempNode.next

    # function for deleting an element in the CDLL
    # for deleting 2nd node , call function with location as
    # any negative value .....
    # Time Complexity : O(n) , Space Complexity : O(1)
    def deleteNode(self, location):
        if self.head is None:
            print("The CDLL DNE")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode
            print("The node has been successfully deleted from CDLL")

    # function to delete the entire CDLL
    # Time Complexity : O(n) , Space Complexity : O(1)
    def deleteCDLL(self):
        if self.head is None:
            print("The CDLL DNE")
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The CDLL has been successfully deleted")
