class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        nse = [0] * n
        stk = []
        for i in range(n):
            while stk and prices[stk[-1]] >= prices[i] :
                idx = stk.pop()
                nse[idx] = prices[i]
            stk.append(i)
        return  [(prices[i] - nse[i]) for i in range(n)]


        
                