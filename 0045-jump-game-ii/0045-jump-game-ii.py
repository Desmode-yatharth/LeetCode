class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        l = r = 0
        farthest = 0
        
        # Loop until the right boundary of the current jump reach target end
        while r < len(nums) - 1:
            # Find the farthest index reachable from current level [l, r]
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            
            # Move to the next level (next jump)
            l = r + 1
            r = farthest
            jumps += 1
            
        return jumps