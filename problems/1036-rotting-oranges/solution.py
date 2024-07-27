class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        rows = len(grid)
        cols = len(grid[0])
        time = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == 2:
                    q.append((x, y))
                if grid[y][x] == 1:
                    fresh += 1
        
        while q and fresh > 0:
            for _ in range(len(q)):
                x,y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx >= 0 and nx < cols and ny >= 0 and ny < rows and grid[ny][nx] == 1:
                        grid[ny][nx] = 2
                        fresh -= 1
                        q.append((nx, ny))
            time += 1
        
        if fresh == 0:
            return time
        else:
            return -1
                    

