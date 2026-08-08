# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def serial_pre(root):
            stk = [root]
            res = []
            while stk :
                node = stk.pop()
                if not node :
                    res.append(None)
                    continue
                res.append(node.val)
                stk.append(node.right)
                stk.append(node.left)
            return res 

        return serial_pre(q) == serial_pre(p)