class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = [0]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(x, y):
            grid[y][x] = "0"
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx >= 0 and ny >= 0 and nx < cols and ny < rows and grid[ny][nx] == "1":
                    dfs(nx, ny)
        
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == "1":
                    islands[0] += 1
                    dfs(x, y)
        
        return islands[0]

