class Solution(object):
    def maxProduct(self, nums):
        nums = [num - 1 for num in nums]
        nums.sort()
        return nums[-2]*nums[-1]
        """
        :type nums: List[int]
        :rtype: int
        """
        