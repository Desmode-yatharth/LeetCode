# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root : return False

        stk = [(root,targetSum - root.val)]
        while stk:
            node,rem = stk.pop()
            if not node.left and not node.right and rem == 0 :
                return True
            
            if node.right : stk.append((node.right,rem - node.right.val ))
            if node.left : stk.append((node.left,rem - node.left.val ))

        return False
        