class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = [] 

    def push(self, value: int) -> None:
        if not self.min_stk or value <= self.min_stk[-1] :
            self.min_stk.append(value)
        self.stk.append(value)
        
    def pop(self) -> None:
        if self.stk[-1] == self.min_stk[-1] : 
            self.min_stk.pop()
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()