class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(len(nums)):
            dp[i] = 1
            for j in range(0,i) :
                if nums[j] < nums[i] :
                    dp[i] = max(dp[i],dp[j] + 1)
        return max(dp)
        