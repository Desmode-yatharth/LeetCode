class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1 : return 0
        stk = []                
        left,right = len(nums) , -1
        for i in range(len(nums)):
            while stk and nums[i] < nums[stk[-1]]:
                idx = stk.pop()
                left = min(left,idx)
            stk.append(i)
        stk = []                
        for i in range(len(nums)-1,-1,-1):
            while stk and nums[i] > nums[stk[-1]]:
                idx = stk.pop()
                right = max(right,idx)
            stk.append(i)
        return right - left + 1 if right != -1 else 0