class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        def sqrt(x):
            if x == 1 : return 1
            lo,hi = 1, x//2
            while lo <= hi :
                mid = lo + (hi-lo)//2
                if mid*mid == x: return mid
                elif mid * mid > x : hi = mid -1
                else : lo = mid + 1 
            return 0.0
        return type(sqrt(num)) == int


        