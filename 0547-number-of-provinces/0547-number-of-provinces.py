class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if len(isConnected) == 0 : return 0
        visit = set()

        def dfs(r):
            if r in visit : return
            visit.add(r)
            for neig in range(len(isConnected)):
                if isConnected[r][neig] == 1 and neig not in visit:
                    dfs(neig)
        
        prov = 0
        for r in range(len(isConnected)):
            if r not in visit:
                prov += 1
                dfs(r)
            
        return prov