# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next : return head
        dum = ListNode(0,head)
        prev,curr = dum,head
        while curr and curr.next :
            if curr.val == curr.next.val : 
                while curr and curr.next and curr.val == curr.next.val :
                    curr = curr.next
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next

        
        return dum.next