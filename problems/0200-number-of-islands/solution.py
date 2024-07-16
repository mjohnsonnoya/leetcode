class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #BFS
        # queue = collections.deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        numislands = 0
        rows = len(grid)
        cols = len(grid[0])
        # def markisland(x, y):
        #     nonlocal numislands
        #     if grid[y][x] == "1":
        #         numislands += 1
        #         grid[y][x] = "0"
        #         queue.append((x, y))
        #         while queue:
        #             x, y = queue.pop()
        #             grid[y][x] = "0"
        #             for dx, dy in directions:
        #                 nx, ny = x + dx, y + dy
        #                 if nx < cols and ny < rows and nx >= 0 and ny >= 0 and grid[ny][nx] == "1":
        #                     queue.append((nx, ny))
    
        # for y in range(rows):
        #     for x in range(cols):
        #         markisland(x, y)
        # return numislands
        def dfs(x, y):
            grid[y][x] = "0"
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx < cols and ny < rows and nx >= 0 and ny >= 0 and grid[ny][nx] == "1":
                    dfs(nx,ny)

        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == '1':
                    numislands += 1
                    dfs(x, y)
        return numislands
