class Solution(object):
    def findMin(self, nums):
        lo,hi=0,len(nums)-1
        res=nums[0]
        while lo <= hi:
            if nums[lo] < nums[hi]:
                res = min(res,nums[lo])
                break
            mid = lo +(hi-lo)//2
            res= min(res,nums[mid])
            if nums[lo] <= nums[mid]:
                # mid is in left sorted array
                #Search right subarray
                lo=mid+1
            else:
                # right sorted array
                # Search in left subarray
                hi = mid-1

        return res



        """
        :type nums: List[int]
        :rtype: int
        """
        