class Queue:
    def __init__(self):
        self.items = []

    # __str__ for printing
    # Time Complexity : O(1) , Space Complexity : O(1)
    def __str__(self):
        if self.items is None:
            return "Empty Queue"
        else:
            values = [str(x) for x in self.items]
            return ' '.join(values)

    # isEmpty() , method
    # Time Complexity : O(1) , Space Complexity : O(1)
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    # enqueue() , method
    # Time Complexity : Amortized Constant , Worst : O(n^2)
    # Space Complexity : O(1)
    def enqueue(self, value):
        self.items.append(value)
        return "Element inserted at end of queue"

    # dequeue() , method
    # Time Complexity : O(n) , Space Complexity : O(1)
    def dequeue(self):
        if self.isEmpty():
            return "Empty Queue"
        else:
            return self.items.pop(0)

    # peek() , method
    # Time Complexity : O(n) , Space Complexity : O(1)
    def peek(self):
        if self.isEmpty():
            return "Empty Queue"
        else:
            return self.items[0]

    # delete() , method
    # Time Complexity : O(1) , Space Complexity : O(1)
    def delete(self):
        self.items = None


# main driver code
q = Queue()
print(q.isEmpty())
q.enqueue(23)
q.enqueue(46)
print(q)
q.dequeue()
q.enqueue(52)
print(q)
print(q.peek())
q.delete()
print(q)
