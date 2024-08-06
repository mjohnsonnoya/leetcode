class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        rows = len(heights)
        cols = len(heights[0])
        
        def BFS(queue, visited):
            while queue:
                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < cols and 0 <= ny < rows and heights[ny][nx] >= heights[y][x] and (nx, ny) not in visited:
                            visited.add((nx, ny))
                            queue.append((nx, ny))
        
        queue1 = collections.deque()
        queue2 = collections.deque()
        for y in range(rows):
            queue1.append((0, y))
            pacific.add((0, y))
            queue2.append((cols - 1, y))
            atlantic.add((cols - 1, y))
        
        for x in range(cols):
            queue1.append((x, 0))
            pacific.add((x, 0))
            queue2.append((x, rows - 1))
            atlantic.add((x, rows - 1))
        
        BFS(queue1, pacific)
        BFS(queue2, atlantic)

        ans = []
        for cell in pacific:
            if cell in atlantic:
                ans.append([cell[1],cell[0]])

        return ans
            
                    

