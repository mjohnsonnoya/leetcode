from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        myqueue = deque()
        fresh_oranges = 0
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        max_minutes = 0
        
        # Initial count and rotten orange positions
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: 
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    myqueue.append((i, j, 0))
        
        # BFS traversal
        while myqueue:
            i, j, minutes = myqueue.popleft()
            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                
                # Check boundaries and if the orange is fresh
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    fresh_oranges -= 1
                    max_minutes = max(max_minutes, minutes + 1)
                    myqueue.append((nx, ny, minutes + 1))
                
        return max_minutes if fresh_oranges == 0 else -1

