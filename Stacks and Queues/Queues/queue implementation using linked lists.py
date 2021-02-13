class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Queue:
    # Time Complexity : O(1) , Space Complexity : O(1)
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)

    # Time Complexity : O(1) , Space Complexity : O(1)
    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode

    # Time Complexity : O(1) , Space Complexity : O(1)
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False

    # Time Complexity : O(1) , Space Complexity : O(1)
    def dequeue(self):
        if self.isEmpty():
            return "Empty Queue"
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.head = None
                self.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode

    # Time Complexity : O(1) , Space Complexity : O(1)
    def peek(self):
        if self.isEmpty():
            return "Empty Queue"
        else:
            return self.linkedList.head

    # Time Complexity : O(1) , Space Complexity : O(1)
    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None


# main driver code
q = Queue()
q.enqueue(14)
q.enqueue(13)
q.enqueue(17)
print(q)
print(q.dequeue())
print(q)
