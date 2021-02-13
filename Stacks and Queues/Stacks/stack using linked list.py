class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    # isEmpty() , method
    # Time Complexity : O(1) , Space Complexity : O(1)
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    # def isFull(self) , is not required for linked list
    # based implementation of a Stack

    # push() , method
    # Time Complexity : O(1) , Space Complexity : O(1)
    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    # pop() , method
    # Time Complexity : O(1) , Space Complexity : O(1)
    def pop(self):
        if self.isEmpty():
            return "Stack Underflow"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue

    # peek() , method
    # Time Complexity : O(1) , Space Complexity : O(1)
    def peek(self):
        if self.isEmpty():
            return "Empty Stack"
        else:
            return self.LinkedList.head.value

    # delete() , method
    # Time Complexity : O(1) , Space Complexity : O(1)
    def delete(self):
        self.LinkedList.head = None


# main driver code
st = Stack()
print(st.isEmpty())
st.push(0)
st.push(1)
st.push(2)
st.push(3)
print("----------")
print(st.peek())
print(st)
