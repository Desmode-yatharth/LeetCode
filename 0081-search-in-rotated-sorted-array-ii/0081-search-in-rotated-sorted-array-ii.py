class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 1 : return target in nums
        lo, hi = 0 , len(nums) - 1
        while lo <= hi :
            mid = lo + (hi-lo)//2
            if nums[mid]  == target : return True
            if nums[mid] == nums[lo] == nums[hi] :
                lo +=1
                hi -= 1
                continue
            elif nums[mid] < nums[lo] : 
                if target > nums[mid] and target <= nums[hi] : lo = mid + 1
                else : hi = mid - 1
            else :
                if target < nums[mid] and target >= nums[lo] : hi = mid - 1
                else : lo = mid + 1
        return False

        
        