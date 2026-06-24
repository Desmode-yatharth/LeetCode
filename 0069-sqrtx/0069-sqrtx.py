class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 : return 0
        lo,hi = 1 , x // 2
        res = 1
        while lo <= hi :
            mid = (hi + lo)//2
            if mid*mid > x :
                hi = mid - 1
            elif mid*mid == x : return mid
            else : 
                res = mid
                lo = mid + 1
        return res
        