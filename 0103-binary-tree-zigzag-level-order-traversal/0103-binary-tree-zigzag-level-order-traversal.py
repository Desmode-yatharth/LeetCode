# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root : return []

        que = deque([root])
        res = []
        flg = 0
        while que : 
            lvl,check = [],len(que)

            for _ in range(check):
                node = que.popleft()
                lvl.append(node.val)
                if node.left : que.append(node.left)
                if node.right : que.append(node.right)
            if flg == 1 : 
                res.append(lvl[::-1])
                flg = 0
            else : 
                res.append(lvl)
                flg = 1

        return res