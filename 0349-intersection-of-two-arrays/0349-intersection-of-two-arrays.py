class Solution(object):
    def intersection(self, nums1, nums2):
        from collections import Counter
        dic1=Counter(nums1)
        dic2=Counter(nums2)
        res=[]
        for key,val in dic1.items():
            if key in dic2:
                res.append(key)

        return res
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        