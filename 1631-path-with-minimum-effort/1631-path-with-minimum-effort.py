import heapq

class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        n, m = len(heights), len(heights[0])

        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        pq = [(0, 0, 0)]                      # (effort so far, r, c)
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while pq:
            d, r, c = heapq.heappop(pq)

            if d > dist[r][c]:                # stale entry, a better path was already found
                continue
            if r == n - 1 and c == m - 1:     # first pop of target is final
                return d

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    nd = max(d, abs(heights[r][c] - heights[nr][nc]))
                    if nd < dist[nr][nc]:
                        dist[nr][nc] = nd
                        heapq.heappush(pq, (nd, nr, nc))

        return 0  # unreachable in a connected grid; only here to satisfy the signature