class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rows = len(grid)
        cols = len(grid[0])
        queue = collections.deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == 1:
                    fresh += 1
                elif grid[y][x] == 2:
                    queue.append((x, y))
        
        t = 0

        while fresh > 0 and queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if ny >= 0 and nx >= 0 and ny < rows and nx < cols and grid[ny][nx] == 1:
                        fresh -= 1
                        grid[ny][nx] = 2
                        queue.append((nx, ny))
            t += 1
        
        if fresh > 0 and not queue:
            return -1
        
        else:
            return t


