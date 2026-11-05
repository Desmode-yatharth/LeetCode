class Solution:
    def partition(self, s: str) -> list[list[str]]:
        
        n = len(s)
        res = []
        path = []

        def dfs(start):
            if start == n:              # whole string consumed
                res.append(path[:])     # copy, not path itself
                return
            for end in range(start, n): # every possible piece end
                piece = s[start:end + 1]
                if piece == piece[::-1]:    # check BEFORE recursing
                    path.append(piece)
                    dfs(end + 1)            # next piece starts after this one
                    path.pop()              # undo

        dfs(0)
        return res
            
        