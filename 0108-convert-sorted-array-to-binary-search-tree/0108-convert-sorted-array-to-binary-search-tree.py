# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums : return None
        self.inord = nums

        def reconst(l,r):
            if l > r: return None

            mid = l + (r - l)//2

            root = TreeNode(self.inord[mid])
            root.left = reconst(l,mid - 1)
            root.right = reconst(mid + 1,r)

            return root
        
        return reconst(0,len(nums)-1)
        