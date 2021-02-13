# using a 3 stacks using a single list
class MultiStack:
    def __init__(self, stackSize):
        self.numberstacks = 3
        self.custList = [0]*(stackSize*self.numberstacks)
        self.sizes = [0]*self.numberstacks
        self.stackSize = stackSize

    # helper function
    def indexOfTop(self, stacknum):
        offset = stacknum*self.stackSize
        return offset+self.sizes[stacknum]-1

    def isFull(self, stacknum):
        if self.sizes[stacknum] == self.stackSize:
            return True
        else:
            return False

    def isEmpty(self, stacknum):
        if self.sizes[stacknum] == 0:
            return True
        else:
            return False

    def push(self, item, stacknum):
        if self.isFull(stacknum):
            return "Stack Overflow"
        else:
            self.sizes[stacknum] += 1
            self.custList[self.indexOfTop(stacknum)] = item

    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            return "Stack Underflow"
        else:
            value = self.custList[self.indexOfTop(stacknum)]
            self.custList[self.indexOfTop(stacknum)] = 0
            self.sizes[stacknum] -= 1
            return value

    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            return "Empty Stack"
        else:
            return self.custList(self.indexOfTop(stacknum))


# main driver code
customStack = MultiStack(6)
print(customStack.isFull(0))
print(customStack.isEmpty(1))
customStack.push(1, 0)
customStack.push(12, 0)
customStack.push(3, 2)
print(customStack.isEmpty(2))
print(customStack.pop(2))
print(customStack.isEmpty(2))
