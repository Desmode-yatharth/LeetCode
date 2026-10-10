from collections import deque , defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        n = numCourses
        adj = defaultdict(list)
        in_deg = [0] * n
        for u , v in prerequisites :
            in_deg[u] += 1
            adj[v].append(u)

        q = deque([i for i in range(n) if in_deg[i] == 0])
        visit = set()

        while q :

            node = q.popleft()
            visit.add(node)
            
            for neigs in adj[node]:
                in_deg[neigs] -= 1

                if in_deg[neigs] == 0 :
                    q.append(neigs)

        if len(visit) != n : return False

        return True