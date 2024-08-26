from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        visited = {}
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(x, y):
            if (x, y) in visited:
                return visited[(x, y)]
            
            ans = 1
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                # Corrected the bounds checking here
                if 0 <= ny < rows and 0 <= nx < cols and matrix[ny][nx] > matrix[y][x]:
                    ans = max(ans, 1 + dfs(nx, ny))
                    
            visited[(x, y)] = ans
            return ans

        ans = 0
        for row in range(rows):
            for col in range(cols):
                ans = max(ans, dfs(col, row,))
                
        return ans

