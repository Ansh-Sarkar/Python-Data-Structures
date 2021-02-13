# defining the main plate stack
class PlateStack:
    # constructor function
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    # makes the stack printable
    def __str__(self):
        return self.stacks

    # used to add an element to the stack while making sure that the capacity is not exceeded
    def push(self, item):
        if len(self.stacks) > 0 and (len(self.stacks[-1])) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])

    # used to return while removing the last element
    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()

    def pop_at(self, stackNumber):
        if len(self.stacks[stackNumber]) > 0:
            return self.stacks[stackNumber].pop()
        else:
            return None


st = PlateStack(2)
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)
print(st.pop())
print(st.pop_at(0))
