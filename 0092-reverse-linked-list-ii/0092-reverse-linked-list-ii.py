# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        last_node_of_first_part = prev
        last_node_of_sub_list = prev.next

        current = prev.next
        prev = None
        for _ in range(right - left + 1):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        last_node_of_first_part.next = prev
        last_node_of_sub_list.next = current
        return dummy.next

            

        
        