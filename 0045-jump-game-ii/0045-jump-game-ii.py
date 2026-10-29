class Solution:
    def jump(self, nums: list[int]) -> int:
        l = r = 0
        jumps = 0
        
        while r < len(nums) - 1:
            reach = 0

            for idx in range(l,r + 1):
                reach = max(reach,nums[idx] + idx)
            
            l,r = r + 1,reach

            jumps += 1

        return jumps
        