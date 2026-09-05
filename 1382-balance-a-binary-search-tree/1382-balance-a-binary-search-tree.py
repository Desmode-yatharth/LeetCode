# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root : return None

        def inorder(root):
            stk,curr = [],root
            res = []
            while stk or curr :
                while curr :
                    stk.append(curr)
                    curr = curr.left
                curr = stk.pop()
                res.append(curr.val)
                curr = curr.right

            return res
        
        self.inord = inorder(root)

        def reconst(l_idx,r_idx):
            if l_idx > r_idx : return None

            mid = l_idx + (r_idx - l_idx)//2

            root = TreeNode(self.inord[mid])
            root.left = reconst(l_idx,mid-1)
            root.right = reconst(mid+1,r_idx)

            return root

        return reconst(0,len(self.inord)-1)


        