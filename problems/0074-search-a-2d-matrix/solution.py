class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def findRow():
            l, m, n = 0, len(matrix) - 1, len(matrix[0])
            while l <= m:
                midrow = l + (m - l)//2
                print(m)
                print("midrow: ", midrow)
                if matrix[midrow][0] <= target <= matrix[midrow][len(matrix[0]) - 1]:
                    return midrow
                if target > matrix[midrow][n - 1]:
                    l = midrow + 1
                else:
                    m = midrow - 1
            return -1
        
        def binarySearch(midrow):
            if midrow == -1:
                return False
            l, r = 0, len(matrix[0]) - 1
            while l <= r:
                m = l + (r - l)//2
                if matrix[midrow][m] == target:
                    return True
                if matrix[midrow][m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return False
        
        midrow = findRow()
        return binarySearch(midrow)
