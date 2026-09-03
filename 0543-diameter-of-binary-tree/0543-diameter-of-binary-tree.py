# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0
        def height(node):
            if not node : return -1
            
            left_h = height(node.left) + 1
            right_h = height(node.right) + 1

            cand = left_h + right_h

            self.best = max(self.best,cand)
            return max(left_h,right_h)
        
        height(root)
        return self.best





        
        