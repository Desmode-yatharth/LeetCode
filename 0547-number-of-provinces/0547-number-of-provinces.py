class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visit =[0]*(n)
        prov = 0
        
        def dfs(node):
            stk = [node]
            while stk :
                node = stk.pop()
                if visit[node] != 0 : continue
                visit[node] = 1
                for neig in range(n):
                    if visit[neig] == 0 and isConnected[node][neig] == 1:
                        stk.append(neig)

        for i in range(n) :
            if visit[i] == 0 :
                prov += 1
                dfs(i)


        
        return prov