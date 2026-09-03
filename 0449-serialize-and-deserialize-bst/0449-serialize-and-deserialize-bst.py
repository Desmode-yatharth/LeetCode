# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root : return ''

        stk,res = [root],''
        while stk :
            node = stk.pop()
            res += str(node.val) + ','
            if node.right : stk.append(node.right)
            if node.left : stk.append(node.left)
        
        return res
        """Encodes a tree to a single string.
        """
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data : return None
        self.pre_idx = 0
        data = data.rstrip(',')
        res = data.split(',')
        def build(low,high):
            if len(res) == self.pre_idx : return None

            root_val = int(res[self.pre_idx])
            if low >= root_val or root_val >= high : return None

            self.pre_idx += 1
            root = TreeNode(root_val)

            root.left = build(low,root_val)
            root.right = build(root_val,high)

            return root

        return build(float('-inf'),float('inf'))








        """Decodes your encoded data to tree.
        """
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans