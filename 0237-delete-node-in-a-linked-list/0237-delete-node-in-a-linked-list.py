# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        prev,curr = None,node

        while curr.next :
            nxt_node = curr.next
            curr.val = nxt_node.val
            prev = curr
            curr = nxt_node
        
        prev.next = None
        
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        