# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head : return head
        curr = head
        small , large = ListNode(0) , ListNode(0)
        p1 , p2 = small , large
        while curr :
            nxt_node = curr.next 
            if curr.val < x :
                p1.next = curr
                p1 = p1.next
            else :
                p2.next = curr
                p2 = p2.next
            curr = nxt_node
        p2.next = None
        p1.next = large.next
        return small.next
