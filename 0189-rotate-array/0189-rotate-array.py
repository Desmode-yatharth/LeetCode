class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if k == 0 or k == n : return
        if k > n : k = k % n
        a,b = nums[n - k :],nums[:n - k]
        nums[n - k :],nums[:n - k] = b,a


        """
        Do not return anything, modify nums in-place instead.
        """
        