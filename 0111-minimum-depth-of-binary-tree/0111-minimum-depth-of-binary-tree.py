# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        if not root : return 0
        min_d = float('inf')

        q = deque([(root,1)])

        while q :
            curr,depth = q.popleft()
            if not curr.left and not curr.right:
                min_d = min(min_d,depth)
            if curr.left : q.append((curr.left,depth+1))
            if curr.right : q.append((curr.right,depth+1))
        return min_d
        