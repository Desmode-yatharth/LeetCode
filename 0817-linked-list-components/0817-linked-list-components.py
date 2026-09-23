# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode | None, nums: list[int]) -> int:
        if not head or len(nums) == 0 : return 0
        if len(nums) == 1 : return 1

        curr,prev = head,None
        check_set = set(nums)
        connect = 0
        while curr :
            if curr.val in check_set and (prev is None or prev.val not in check_set):   connect += 1
            prev = curr
            curr = curr.next
            
        return connect
                
            
            


            

            

        