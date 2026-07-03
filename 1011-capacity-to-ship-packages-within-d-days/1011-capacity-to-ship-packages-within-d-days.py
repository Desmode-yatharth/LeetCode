class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo , hi = max(weights) , sum(weights)
        res = 0
        def check_days(mid):
            num_days,curr_sum = 0,0
            for w in weights :
                if w > mid : return float('inf')
                if curr_sum + w > mid : 
                    num_days += 1
                    curr_sum = 0
                curr_sum += w
            return num_days + 1
        
        while lo <= hi :
            mid = lo + (hi - lo)//2
            num_days = check_days(mid)
            if num_days <= days : 
                res = mid
                hi = mid - 1 
            else : lo = mid + 1
        return res
                
        