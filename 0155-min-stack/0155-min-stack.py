class MinStack:

    def __init__(self):
        self.stk = []
        self.curr_min = float('inf') 

    def push(self, value: int) -> None:
        self.curr_min = min(value,self.curr_min)
        self.stk.append([value,self.curr_min])      
    
    def pop(self) -> None:
        self.stk.pop()
        if len(self.stk) == 0 : self.curr_min = float('inf')
        else : self.curr_min = self.stk [-1][1]
        
    def top(self) -> int:
        return self.stk[-1][0]
    def getMin(self) -> int:
        return self.stk[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()