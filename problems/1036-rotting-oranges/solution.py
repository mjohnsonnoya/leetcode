class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        time = 0
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == 2:
                    q.append((x, y))
                if grid[y][x] == 1:
                    fresh += 1
        
        while q and fresh > 0:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (nx < 0 or nx >= cols or
                        ny < 0 or ny >= rows or
                        grid[ny][nx] != 1):
                        continue
                    grid[ny][nx] = 2
                    q.append((nx, ny))
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1
