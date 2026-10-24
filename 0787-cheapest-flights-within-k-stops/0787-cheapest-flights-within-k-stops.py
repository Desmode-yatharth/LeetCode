import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))

        pq = [(0, src, k + 1)]
        visit = set()

        while pq:
            curr_dist, node, stop_left = heapq.heappop(pq)

            if node == dst:
                return curr_dist

            if (node, stop_left) in visit:
                continue
            visit.add((node, stop_left))

            if stop_left == 0:
                continue

            for neig, w in adj[node]:
                if (neig, stop_left - 1) not in visit:
                    heapq.heappush(pq, (curr_dist + w, neig, stop_left - 1))

        return -1