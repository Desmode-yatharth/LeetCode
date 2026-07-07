class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk  = []
        n = len(temperatures)
        ans = [0] * n
        stk.append(0)
        for i in range(1,n):
            while len(stk) != 0 :
                idx = stk[-1]
                if temperatures[i] > temperatures[idx] :
                    ans[idx] = i - idx
                    stk.pop()
                else: break
            stk.append(i)
        return ans


        