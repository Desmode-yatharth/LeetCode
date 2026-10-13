from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        cells = deque([[entrance[0], entrance[1], 0]])
        maze[entrance[0]][entrance[1]] = "+"
        m,n = len(maze), len(maze[0])
        while cells:
            i,j,k = cells.popleft()
            check = [[i-1,j], [i+1,j], [i,j+1], [i,j-1]]
            for r,c in check:
                if r >= 0 and c >= 0 and r < m and c < n and maze[r][c] == ".":
                    if r == 0 or c == 0 or r == m-1 or c == n-1:
                        return k+1
                    cells.append([r,c,k+1])
                    maze[r][c] = "+"
        return -1