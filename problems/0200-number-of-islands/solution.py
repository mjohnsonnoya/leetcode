class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(col, row):
            if (0 <= col < cols and 0 <= row < rows and grid[row][col] != "0"):
                grid[row][col] = "0"
                for dx, dy in directions:
                    dfs(col + dx, row + dy)
            return
            
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    count += 1
                    dfs(col, row)
        return count

            
            


