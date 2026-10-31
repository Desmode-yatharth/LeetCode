class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        MOD = 10**9 + 7
        adj = [[] for _ in range(n)]
        for u, v, w in roads:          # undirected; drop second line if directed
            adj[u].append((v, w))
            adj[v].append((u, w))

        INF = float('inf')
        dist = [INF] * n
        ways = [0] * n
        dist[0], ways[0] = 0, 1
        pq = [(0, 0)]

        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:            # stale entry, skip
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:       # strictly better: reset the count
                    dist[v] = nd
                    ways[v] = ways[u]
                    heapq.heappush(pq, (nd, v))
                elif nd == dist[v]:    # equally good: add the count
                    ways[v] = (ways[v] + ways[u]) % MOD
        return ways[n - 1]
        