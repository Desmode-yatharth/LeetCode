from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res =[]
        if len(nums1) > len(nums2) :
            hash_map = Counter(nums2)
            for i in nums1 :
                if i in hash_map and hash_map[i] >= 1 : 
                    res.append(i)
                    hash_map[i] -= 1
        else :
            hash_map = Counter(nums1)
            for i in nums2 :
                if i in hash_map and hash_map[i] >= 1 : 
                    res.append(i)
                    hash_map[i] -= 1        
        return res
            

        