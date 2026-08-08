# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        que = deque([root])
        res = []

        while que:
            lvl , l_check = [],len(que)
            for _ in range(l_check):
                node = que.popleft()
                if not node :
                    lvl.append(None)
                    continue
                lvl.append(node.val)
                que.append(node.left)
                que.append(node.right)
            res.append(lvl)
        
        for i in res:
            if i != i[::-1]: return False
        return True
