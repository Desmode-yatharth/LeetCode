class Solution:
    def solve(self, board: list[list[str]]) -> None:
        n,m = len(board),len(board[0])

        def dfs(r,c):
            if r < 0 or r >= n or c < 0 or  c >= m or board[r][c] == 'X' or board[r][c] == 'S': return
            board[r][c] = "S"

            dfs(r + 1,c)
            dfs(r - 1,c)
            dfs(r,c + 1)
            dfs(r,c - 1)
        
        for r in range(n):
            for c in range(m):
                if (r == 0 or r == n-1 or c == 0 or c == m-1) and board[r][c] == 'O':
                    dfs(r,c)
        
        for r in range(n):
            for c in range(m):
                if board[r][c] == "O":
                    board[r][c] = 'X'
                elif board[r][c] == "S":
                    board[r][c] = 'O'

        """
        Do not return anything, modify board in-place instead.
        """
        