# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root : return 0
        if not root.left and not root.right : return root.val
        
        self.max_sum = float('-inf')

        def pathSum(node):
            if not node : return 0
            
            left_sum = pathSum(node.left) 
            right_sum = pathSum(node.right)
            
            bst_left = max(0,left_sum)
            bst_right = max(0,right_sum)
            
            self.max_sum = max(self.max_sum,node.val + bst_left + bst_right)

            return node.val + max(bst_left , bst_right)

        pathSum(root)
        return self.max_sum
        