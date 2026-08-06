# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root : return []
        stk = []
        res = []
        curr = root

        while stk or curr :
            while curr :
                stk.append(curr)
                curr = curr.left
            
            node = stk.pop()
            res.append(node.val)

            curr = node.right if node.right else None

        return res