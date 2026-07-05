class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i , j = 0,0
        max_diff = 0

        while i < len(nums1) and j < len(nums2) :
            if nums2[j] < nums1[i]: 
                i +=1
            else : 
                max_diff = max(max_diff , j - i)
                j +=1
        return max_diff
        