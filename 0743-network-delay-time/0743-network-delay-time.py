class Solution:
    import heapq
    from collections import defaultdict
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:

        adj = defaultdict(list)
        for u,v,w in times :
            adj[u].append((v,w))

        print(adj)

        dist = [float('inf')]*(n+1)
        dist[k] = 0
        visit = set()
        pq = [(0,k)]

        while pq :
            curr_dist , node = heapq.heappop(pq)

            if node in visit : continue
            visit.add(node)

            for neig , w in adj[node]:
                if neig not in visit :
                    dist_n = curr_dist + w
                    if dist_n < dist[neig] :
                        dist[neig] = dist_n
                        heapq.heappush(pq,(dist_n,neig))
        print(dist)
        return max(dist[1:]) if max(dist[1:]) != float('inf') else -1
        