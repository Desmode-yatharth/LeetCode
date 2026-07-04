class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                left = right + 1
            max_len = max(max_len, right - left + 1)
        return max_len