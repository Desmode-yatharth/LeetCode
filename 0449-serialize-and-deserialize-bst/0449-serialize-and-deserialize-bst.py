# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        s = []

        def ser(root):
            if not root:
                s.append('N')
                return
            s.append(str(root.val))
            ser(root.left)
            ser(root.right)

        ser(root)
        news = ",".join(s)
        return news

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if data is "":
            return None
        
        vars = iter(data.split(","))

        def deser():
            var = next(vars)
            if var == 'N':
                return None

            node = TreeNode(var)
            node.left = deser()
            node.right = deser()

            return node

        return deser()
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans