class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        k = inorder.index(root_val)
        n = k  # number of nodes in left subtree

        root.left = self.buildTree(preorder[1:1+n], inorder[:k])
        root.right = self.buildTree(preorder[1+n:], inorder[k+1:])

        return root