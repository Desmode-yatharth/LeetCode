# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next or left == right : return head

        def reverse(head,end):
            prev,curr = None,head
            new_tail = head
            while curr != end :
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return [prev,new_tail]

        dum = ListNode(0,head)
        prev = dum
        idx = 1
        for _ in range(right):
            if idx == left : 
                prev_old_head = prev
            idx += 1
            prev = prev.next
            
        # print(prev,"\n",prev_old_head)
        end = prev.next
        new_h ,new_t = reverse(prev_old_head.next,prev.next)

        prev_old_head.next = new_h
        new_t.next = end

        return dum.next

        