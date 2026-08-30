# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root : return 0
        max_depth = float('-inf')
        stk = [(root,1)]
        while stk:
            node,dep = stk.pop()
            max_depth = max(max_depth,dep)
            if node.right : stk.append((node.right,dep+1))
            if node.left : stk.append((node.left,dep+1))

        return max_depth
        