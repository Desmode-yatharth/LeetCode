# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root : return []

        que = deque([root])
        res = []
        
        while que : 
            lvl,check_pops = [] ,len(que)

            for _ in range(check_pops):
                node = que.popleft()
                lvl.append(node.val)
                if node.left : que.append(node.left)
                if node.right : que.append(node.right)
            
            res.append(lvl)
            
        p1,p2 = 0,len(res)-1
        while p1 < p2 :
            res[p1],res[p2] = res[p2],res[p1]
            p1+=1
            p2-=1
        return res