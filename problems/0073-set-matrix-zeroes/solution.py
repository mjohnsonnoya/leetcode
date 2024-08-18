class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        rowZero = False

        for i in range(rows):
            for j in range(cols):
                if i == 0 and matrix[i][j] == 0:
                    rowZero = True
                elif j == 0 and matrix[i][j] == 0:
                    matrix[0][0] = 0
                elif matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[0][j] == 0:
                    matrix[i][j] = 0
                if matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for row in range(rows):
                matrix[row][0] = 0
        
        if rowZero:
            for col in range(cols):
                matrix[0][col] = 0


        
