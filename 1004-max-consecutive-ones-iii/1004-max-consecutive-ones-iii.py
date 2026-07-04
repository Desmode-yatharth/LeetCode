class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = 0
        left = 0
        zeroes = 0
        for right in range(len(nums)):
            curr_bit = nums[right]
            zeroes += int(curr_bit == 0)
            while zeroes > k :
                leave_bit = nums[left]
                if leave_bit == 0 : zeroes -=1
                left += 1
            max_len = max(max_len , right - left + 1)
        return max_len
            
        