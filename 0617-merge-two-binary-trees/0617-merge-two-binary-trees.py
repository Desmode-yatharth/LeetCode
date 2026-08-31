# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 : return root2
        if not root2 : return root1
        merged = TreeNode(root1.val + root2.val)
        stk = [(merged,root1,root2)]
        

        while stk :
            merg,n1,n2 = stk.pop()

            if n1.left and n2.left :
                merg.left = TreeNode(n1.left.val + n2.left.val)
                stk.append((merg.left,n1.left,n2.left))
            else:
                merg.left = n1.left or n2.left

            if n1.right and n2.right :
                merg.right = TreeNode(n1.right.val + n2.right.val)
                stk.append((merg.right,n1.right,n2.right))
            else:
                merg.right = n1.right or n2.right

        return merged

        