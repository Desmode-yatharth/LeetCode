class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        candA = nums[-1] * nums[-2] * nums[-3]
        candB = nums[0]   * nums[1]   * nums[-1]
        answer = max(candA, candB)
        return answer