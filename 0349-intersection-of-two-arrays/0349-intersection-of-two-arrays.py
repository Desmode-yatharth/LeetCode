class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n,m = len(nums1), len(nums2)
        res = set()
        if n < m : 
            hash_set = set(nums1)
            for i in nums2 :
                if i in hash_set :
                    res.add(i)
        else : 
            hash_set = set(nums2)
            for i in nums1 :
                if i in hash_set :
                    res.add(i)

        return list(res)

        
        