class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        num_islands = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "0":
                    continue
                else:
                    num_islands += 1
                    q = deque()
                    q.append((row, col))
                    grid[row][col] = "0"
                    while q:
                        r, c = q.popleft()
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if (0 <= nr < m) and (0 <= nc < n) and grid[nr][nc] == "1":
                                q.append((nr, nc))
                                grid[nr][nc] = "0"

        return num_islands
                

