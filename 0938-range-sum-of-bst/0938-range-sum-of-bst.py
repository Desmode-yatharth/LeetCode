# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        stk = [root]
        res = 0

        while stk:
            node = stk.pop()
            if not node:
                continue

            # include if in range
            if low <= node.val <= high:
                res += node.val

            # BST pruning
            if node.val > low:
                stk.append(node.left)
            if node.val < high:
                stk.append(node.right)
        return res
        

        