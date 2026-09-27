class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        
        from collections import deque
        n = len(graph)
        visit = [-1] * (n) 
        
        for start in range(n):
            if visit[start] != -1 : continue
            visit[start] = 0  
            q = deque([start])
            while q :
                node = q.popleft()   
                curr_col = 0 if visit[node] == 1 else 1
                for neigs in graph[node]:    
                    if visit[neigs] == -1:
                        visit[neigs] = curr_col
                        q.append(neigs)
                    elif visit[neigs] == visit[node] : 
                        return False
        return True
                        
