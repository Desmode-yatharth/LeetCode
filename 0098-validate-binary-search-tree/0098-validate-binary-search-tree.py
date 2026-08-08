# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root : return False

        stk , curr = [] , root
        res = []
        while stk or curr :
            while curr :
                stk.append(curr)
                curr = curr.left
            curr = stk.pop()
            res.append(curr.val)
            if len(res) > 1 and res[-1] <= res[-2]: return False

            curr = curr.right

        return True


        