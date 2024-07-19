class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        rows = len(grid)
        cols = len(grid[0])
        def dfs(x, y):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            if x < 0 or y < 0 or y > rows - 1 or x > cols - 1 or grid[y][x] == 0:
                return 0
            else:
                grid[y][x] = 0
                ans = 1
                for dx, dy in directions:
                    ans += dfs(x + dx, y + dy)
                return ans
        
        for y in range(rows):
            for x in range(cols):
                maxarea = max(maxarea, dfs(x, y))

        return maxarea


