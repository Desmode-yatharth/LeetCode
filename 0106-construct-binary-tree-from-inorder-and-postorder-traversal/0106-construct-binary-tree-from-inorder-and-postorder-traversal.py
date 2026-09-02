# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder : return None
        self.idx_map = {val:i for i,val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1

        def build(left_in,right_in):
            if left_in > right_in : return None

            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)

            mid = self.idx_map[root_val]

            
            root.right = build(mid + 1,right_in)
            root.left = build(left_in,mid - 1)
            
            return root

        return build(0,len(postorder) - 1)


        