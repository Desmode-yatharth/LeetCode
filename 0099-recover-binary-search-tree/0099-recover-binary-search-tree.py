# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        stk,curr = [],root
        f,s = None,None
        prev = None
        while stk or curr :
            while curr :
                stk.append(curr)
                curr = curr.left
            curr = stk.pop()

            if prev and prev.val > curr.val :
                if not f : f = prev
                s = curr
            prev = curr
            curr = curr.right

        f.val , s.val = s.val,f.val


            

        """
        Do not return anything, modify root in-place instead.
        """
        