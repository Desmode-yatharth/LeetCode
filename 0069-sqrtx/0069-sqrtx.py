class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1 : return x
        lo,hi = 1 , x // 2
        while lo <= hi :
            mid = (hi + lo)//2
            if mid*mid > x : hi = mid - 1
            elif mid*mid == x : return mid
            else : lo = mid + 1
        return hi
        