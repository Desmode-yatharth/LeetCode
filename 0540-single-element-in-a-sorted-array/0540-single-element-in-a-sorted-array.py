class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1 : return nums[0]
        n = len(nums)
        if nums[0] != nums[1] : return nums[0]
        if nums[n-1] != nums[n-2] : return nums[n-1]
        lo,hi = 1 , n - 2
        while lo <= hi :
            mid = lo + (hi - lo)//2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1] : return nums[mid]
            elif nums[mid] == nums[mid + 1]  and mid % 2 == 0 : 
                lo = mid + 1
            elif nums[mid] == nums[mid + 1]  and mid % 2 != 0 : hi = mid - 1
            elif nums[mid] == nums[mid - 1]  and mid % 2 == 0 : hi = mid - 1
            else : lo = mid + 1
            
            
        
        