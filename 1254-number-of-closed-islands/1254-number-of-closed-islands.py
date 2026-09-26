class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        n,m = len(grid),len(grid[0])

        def dfs(r,c):
            if r < 0 or  r >= n or c < 0 or c >= m or grid[r][c] == 1:
                return
            
            grid[r][c] = 1
            dfs(r + 1,c)
            dfs(r - 1,c)
            dfs(r,c + 1)
            dfs(r,c - 1)
        
        for r in range(n):
            for c in range(m):
                if (r == 0 or r == n - 1 or c == 0 or c == m - 1) and grid[r][c] == 0:
                    dfs(r,c)
    
        count_unr = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0 : 
                    dfs(r,c)
                    count_unr += 1

        return count_unr
        