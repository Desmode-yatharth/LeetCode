# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root : return 0

        range_sum = 0
        stk , curr = [],root

        while stk or curr:
            while curr :
                stk.append(curr)
                curr = curr.left
            curr = stk.pop()
            if curr.val in range(low,high + 1): range_sum += curr.val  
            curr = curr.right
        return range_sum
        