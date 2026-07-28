# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next : return head
        dum = ListNode(0,head)
        prev = head
        curr = head.next
        while curr :
            if prev.val != curr.val :
                prev.next = curr
                prev = prev.next
            curr = curr.next
        if prev.next and prev.val == prev.next.val : prev.next = None
                
        return dum.next


        