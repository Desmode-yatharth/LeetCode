# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root : return 0
        prev,curr,stk = None,root,[]
        min_d = float('inf')

        while stk or curr:
            while curr:
                stk.append(curr)
                curr = curr.left
            curr = stk.pop()
            if prev:
                min_d = min(min_d,curr.val-prev.val)
            prev = curr
            curr = curr.right

        return min_d