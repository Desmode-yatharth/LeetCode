# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder : return None
        self.idx_map = {val : i for i,val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1

        def build(left_idx,right_idx):
            if left_idx > right_idx : return None

            node_v = postorder[self.post_idx]
            self.post_idx -= 1
            node = TreeNode(node_v)
            mid = self.idx_map[node_v]

            node.right = build(mid + 1, right_idx)
            node.left = build(left_idx , mid - 1)

            return node
        return build(0,len(inorder) - 1)
            

        