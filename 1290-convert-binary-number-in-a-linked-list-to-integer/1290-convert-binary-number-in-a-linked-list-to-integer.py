# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        if not head : return
        new_num = 0
        while head:
            new_num = new_num*2 + head.val
            head = head.next
        return new_num
        