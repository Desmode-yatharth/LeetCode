# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root : return False
        prev_val = float('-inf')

        stk,curr = [],root
        while stk or curr :
            while curr:
                stk.append(curr)
                curr = curr.left

            curr = stk.pop()
            if prev_val >= curr.val : return False
            prev_val = curr.val
            curr = curr.right

        
        return True