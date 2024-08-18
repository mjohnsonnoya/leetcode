class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        while l < r:
            top, bottom = l, r
            left, right = l, r

            for i in range(r - l):
                topleft = matrix[top][left + i]
                
                matrix[top][left + i] = matrix[bottom - i][left]

                matrix[bottom - i][left] = matrix[bottom][right - i]

                matrix[bottom][right - i] = matrix[top + i][right]

                matrix[top + i][right] = topleft
            l += 1
            r -= 1

