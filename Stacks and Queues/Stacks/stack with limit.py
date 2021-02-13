class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    # isEmpty() , method
    # Time Complexity : O(1) , Space Complexity : O(1)
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # isFull() , method
    # Time Complexity : O(1) , Space Complexity : O(1)
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    # push() , method
    # Time Complexity : Amortized Constant O(n) or O(n^2)
    # Space Complexity
    def push(self, value):
        if self.isFull():
            return "Stack Overflow"
        else:
            self.list.append(value)
            return "The element has been pushed successfully"

    # pop() , method
    # Time Complexity : O(1) , Space Complexity : O(1)
    def pop(self):
        if self.isEmpty():
            return "Underflow"
        else:
            return self.list.pop()

    # peek() , method
    # Time Complexity : O(1) , Space Complexity : O(1)
    def peek(self):
        if self.isEmpty():
            return "Empty Stack"
        else:
            return self.list[-1]

    # delete() , method
    # Time complexity : O(1) , Space Complexity : O(1)
    def delete(self):
        self.list = None


# main driver code
st = Stack(4)
print(st.isEmpty())
print(st.isFull())
st.push(0)
st.push(1)
print(st)
