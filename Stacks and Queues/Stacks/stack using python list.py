# Time Complexity : O(1) , Space Complexity : O(1)
class Stack:
    def __init__(self):
        self.list=[]
    
    def __str__(self):
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return '\n'.join(values)
    
    # isEmpty() , method
    # Time Complexity : O(1) , Space Complexity : O(1)
    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False
        
    # push() , method
    # Time Complexity : Amortized Constant (remember)
    # can get pushed to O(n^2) in worst case
    # Space Complexity : O(1)
    def push(self,value):
        self.list.append(value)
        return "The element has been successfully inserted"
    
    # pop() , method
    # Time Complexity : O(1) , Space Complexity : O(1)
    def pop(self):
        if self.list==[]:
            return "Stack Underflow"
        else:
            return self.list.pop()
        
    # peek() , method
    # Time Complexity : O(1) , Space Complexity : O(1)
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.list[len(self.list)-1]
        
    # delete() , method
    # Time Complexity : O(1) , Space Complexity : O(1)
    def delete(self):
        self.list=None
        
# main driver code
st=Stack()
st.push(1)
st.push(20)
st.push(30)
print(st.peek())