# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head : return None
        self.pre = []
        curr = head
        while curr:
            self.pre.append(curr.val)
            curr = curr.next
        
        def build(l,r):
            if l > r : return None

            mid = l + (r - l)//2

            root = TreeNode(self.pre[mid])
            root.left = build(l,mid - 1)
            root.right = build(mid + 1,r)
            return root

        return build(0,len(self.pre)-1)

        