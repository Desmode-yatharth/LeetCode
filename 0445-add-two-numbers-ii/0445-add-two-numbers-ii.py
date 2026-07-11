# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stk1 , stk2 = [] , []
        head = None
        while l1 :
            stk1.append(l1.val)
            l1 = l1.next
        while l2 :
            stk2.append(l2.val)
            l2 = l2.next
        carry = total = 0
        
        while stk1 or stk2 or carry:
            total = carry
            if stk1 :
                total += stk1.pop()
            if stk2 :
                total += stk2.pop()
            new_num = total % 10
            carry = total // 10
            curr = ListNode(new_num)
            curr.next = head
            head = curr

        
        return head





        