class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.visit = set()

        def dfs(r):
            stk = [r]
            while stk :
                node = stk.pop()
                
                if node in self.visit: continue
                self.visit.add(node)
                
                for n in range(len(isConnected)):
                    if isConnected[node][n] == 1 and n not in self.visit :
                        stk.append(n)



        prov = 0
        for r in range(len(isConnected)):
                if r not in self.visit : 
                    dfs(r)
                    prov += 1

        return prov