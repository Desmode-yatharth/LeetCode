class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_deg = [0] * (n+1)
        out_deg = [0] * (n+1)
        for u,v in trust :
            in_deg[u] += 1
            out_deg[v] += 1
        j = -1
        for itr in range(1,n + 1):
            if in_deg[itr] == 0 and out_deg[itr] == n - 1 :
                if j == -1: j = itr
                else : return -1
        return j
