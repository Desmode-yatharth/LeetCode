# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head.next or k == 1 : return head
        def reverse(head,next_head):
            curr,prev = head,None
            new_tail = head
            while curr != next_head :
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return [new_tail,prev] # prev = new-head
        
        dum = ListNode()
        prev = dum
        old_next_head = curr = head
        idx = 1
        while curr :
            next_head = curr.next 
            if idx % k == 0 :  
                new_tail,new_head = reverse(old_next_head,next_head)
                new_tail.next = next_head
                prev.next = new_head
                old_next_head = next_head
                prev = new_tail
            idx += 1
            curr = next_head 
            
        return dum.next



        



        


        