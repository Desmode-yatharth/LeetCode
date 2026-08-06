# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root : return []

        stk = [root]
        res = [] 

        while stk :
            node = stk.pop()
            res.append(node.val)

            if node.left : stk.append(node.left)
            if node.right : stk.append(node.right)

        p1 , p2 = 0, len(res) - 1

        while p1 < p2 :
            res[p1],res[p2] = res[p2],res[p1]
            p1 += 1
            p2 -= 1

        return res

        return inter