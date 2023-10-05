import queue
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        myqueue = queue.Queue()
        in_island = [[0 for _ in range(n)] for _ in range(m)]
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        num_islands = 0
        
        def is_valid(i,j):
                return 0 <= i < m and 0 <= j < n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not in_island[i][j]:
                    myqueue.put((i, j))
                    num_islands += 1  # Start a new island
                    while not myqueue.empty():
                        x, y = myqueue.get()
                        in_island[x][y] = 1
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if is_valid(nx, ny) and grid[nx][ny] == '1' and not in_island[nx][ny]:
                                myqueue.put((nx, ny))
                                in_island[nx][ny] = 1

        return num_islands
