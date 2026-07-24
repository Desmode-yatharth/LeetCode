# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head : return
        dum = ListNode()
        dum.next = head
        left , right = dum , dum
        for _ in range(n):
            right = right.next
        while right.next :
            left = left.next
            right = right.next
        next_node = left.next.next
        left.next = next_node
        return dum.next


