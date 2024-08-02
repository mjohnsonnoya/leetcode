class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        queue = collections.deque()
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        rows = len(grid)
        cols = len(grid[0])

        def dfs(x, y):
            area = 1
            grid[y][x] = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx >= 0 and ny >= 0 and nx < cols and ny < rows and grid[ny][nx] == 1:
                    area += dfs(nx, ny)
            return area
        
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == 1:
                    maxarea = max(dfs (x, y), maxarea)

        
        return maxarea


