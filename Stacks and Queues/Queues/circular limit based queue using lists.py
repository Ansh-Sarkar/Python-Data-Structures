class Queue:
    # Time Complexity : O(1) , Space Complexity : O(n)
    def __init__(self, maxSize):
        self.items = maxSize*[None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    # Time Complexity : O(1) , Space Complexity : O(1)
    def isFull(self):
        if (self.top+1 == self.start) or (self.start == 0 and self.top+1 == self.maxSize):
            return True
        else:
            return False

    # Time Complexity : O(1) , Space Complexity : O(1)
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    # Time Complexity : O(1) , Space Complexity : O(1)
    def enqueue(self, value):
        if self.isFull():
            return "Queue Overflow"
        else:
            if self.top+1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element has been inserted"

    # Time Complexity : O(1) , Space Complexity : O(1)
    def dequeue(self):
        if self.isEmpty():
            return "Empty Queue"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start+1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement

    # Time Complexity : O(1) , Space Complexity : O(1)
    def peek(self):
        if self.isEmpty():
            return "Empty Queue"
        else:
            return self.items[self.start]

    # Time Complexity : O(1) , Space Complexity : O(1)
    def delete(self):
        self.items = self.maxSize*[None]
        self.top = -1
        self.start = -1


# main driver code
q = Queue(3)
print(q.isFull())
print(q.isEmpty())
q.enqueue(14)
q.enqueue(17)
q.enqueue(20)
q.enqueue(27)
print(q)
print(q.isFull())
print(q.dequeue())
print(q)
print(q.isFull())
q.delete()
print(q)
