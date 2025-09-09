class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        q = deque()
        time = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    q.append((row, col))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while q:
            level = len(q)
            time += 1
            for _ in range(level):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < m) and (0 <= nc < n) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    return -1

        return max(0, time - 1)
            
