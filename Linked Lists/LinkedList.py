from random import randint

# node class definition


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

# defining the linked list class


class LinkedList:
    # initialization function
    def __init__(self, values=None):
        self.head = None
        self.tail = None

    # iterater function
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

    # string returning function
    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)

    # length returning function
    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    # function to append value to end of list or create
    # a new list if list not present
    def add(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    # function to generate a random linked list of some
    # size 'n' within a given range .
    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self
