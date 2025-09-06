class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        q = deque()

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    q.append((row, col))


        time = 0
        while q:
            level = len(q)          # snapshot the current minute's items
            progressed = False
            for _ in range(level):  # <-- use the snapshot, not len(q)
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        progressed = True
            if progressed:
                time += 1
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    return -1
        
        return time

            



        
