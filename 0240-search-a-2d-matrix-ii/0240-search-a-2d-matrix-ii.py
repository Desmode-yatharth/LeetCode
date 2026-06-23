class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i,j = 0,len(matrix[0]) - 1
        start = matrix[i][j]
        while j >= 0 and i < len(matrix) :
            if matrix[i][j] > target :
                 j-=1
            elif matrix[i][j] < target :
                i +=1
            else : return True
        return False

        