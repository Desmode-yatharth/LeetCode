class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        if len(matrix) == 1 : return [0]
        n = len(matrix)
        ans = [0]*n
        for row in range(n):
            print(matrix[row])
            ans[row] = matrix[row].count(1)
        return ans