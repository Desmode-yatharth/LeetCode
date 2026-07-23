class ListNode:
    def __init__(self,val):
        self.url = val
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)
        self.hist = 0

    def visit(self, url: str) -> None:
        new_curr = ListNode(url)
        new_curr.prev = self.curr
        self.curr.next = new_curr
        self.curr = new_curr

    def back(self, steps: int) -> str:
        while steps > 0 and self.curr.prev :
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.url
        
    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr.next :
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)