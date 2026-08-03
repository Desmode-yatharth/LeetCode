# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        curr,nxt = node,node.next
        curr.val = nxt.val
        curr.next = nxt.next
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        