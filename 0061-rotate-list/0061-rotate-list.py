# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0 : return head

        len_ll = 1
        curr = head
        while curr.next :
            len_ll += 1
            curr = curr.next
        k = k % len_ll
        if k == 0 : return head
        
        old_tail = curr
        old_tail.next = head

        n = len_ll - k
        
        curr = head
        while n > 1 :
            curr = curr.next
            n -= 1
        
        new_tail = curr
        new_head = new_tail.next
        new_tail.next = None
    
        return new_head
            

        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        