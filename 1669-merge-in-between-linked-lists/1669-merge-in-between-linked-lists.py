# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        prev = ListNode()
        prev.next = list1

        curr = list1
        count = 0
        while count <= b  :
            if count == a - 1  : start = curr
            count += 1
            curr = curr.next
        last = curr

        start.next = list2
        while start.next :
            start = start.next
        start.next = last

        return prev.next


            
        


