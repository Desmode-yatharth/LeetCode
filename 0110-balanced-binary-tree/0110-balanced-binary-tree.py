# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root : return True
        def height(node):
            if not node : return 0 , True

            h_l,left_bal = height(node.left)
            h_r,right_bal = height(node.right)
            
            if abs(h_l - h_r) <= 1 and left_bal and right_bal : 
                return 1 + max(h_l,h_r) , True

            return 1 + max(h_l,h_r) , False
        
        height , is_true = height(root)
        return is_true == True
        

        