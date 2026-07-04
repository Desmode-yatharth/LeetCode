class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0 : return 0 
        count_subarr = 0
        # for i in nums : 
        #     if i < k : count_subarr += 1
        left = 0
        curr_prod = 1
        for right in range(len(nums)) :
            curr_num = nums[right]
            curr_prod *= curr_num
            while curr_prod >= k :
                leave_num = nums[left]
                curr_prod //= leave_num
                left +=1
            count_subarr += right - left + 1
        return count_subarr



        