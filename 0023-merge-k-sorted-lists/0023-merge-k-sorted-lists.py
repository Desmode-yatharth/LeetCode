# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        def merge(l1,l2):
            dum = ListNode()
            prev = dum
            while l1 and l2 :
                if l1.val < l2.val : 
                    prev.next = l1
                    prev,l1 = l1,l1.next
                else: 
                    prev.next = l2
                    prev,l2 = l2,l2.next
            if l1 or l2 : prev.next = l1 if l1 else l2
            return dum.next
        if not lists : return
        first_l = lists[0]
        for i in range(1,len(lists)):
            second_l = lists[i]
            first_l = merge(first_l,second_l)

        return first_l
        
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        