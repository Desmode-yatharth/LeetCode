# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next : return head
        slow,fast = head,head
        def reverse(head):
            curr,prev = head,None
            while curr :
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        sec_sub_tail = slow.next
        slow.next = None
        new_sec_head = reverse(sec_sub_tail)
        p1 , p2 = head , new_sec_head
        
        flg = 0
        while p1 and p2 :
            nxt1 , nxt2 = p1.next , p2.next
            
            if flg == 0 :
                p1.next = p2
                p1 = nxt1
                flg = 1
            else:
                p2.next = p1
                p2 = nxt2
                flg = 0
                
        return head

                

        """
        Do not return anything, modify head in-place instead.
        """
        