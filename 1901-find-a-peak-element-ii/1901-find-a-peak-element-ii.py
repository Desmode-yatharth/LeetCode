class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            maxE = 0
            for i in range(m):
                if mat[i][mid] > mat[maxE][mid]:
                    maxE = i
            curr = mat[maxE][mid]
            right = mat[maxE][mid + 1] if mid < n - 1 else -1
            left = mat[maxE][mid - 1] if mid > 0 else -1
            if curr > right and curr > left:
                return[maxE, mid]
            elif curr < right: 
                l = mid + 1
            else:
                r = mid - 1