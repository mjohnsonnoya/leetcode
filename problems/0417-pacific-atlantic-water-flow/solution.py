class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        def bfs(queue, visited):
            for x, y in visited:
                queue.append((x, y))
            while queue:
                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    visited.add((x, y))
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if nx >= 0 and ny >= 0 and nx < cols and ny < rows and heights[ny][nx] >= heights[y][x] and (nx, ny) not in visited:
                            visited.add((nx, ny))
                            queue.append((nx, ny))
        
        for y in range(rows):
            pacific.add((0, y))
            atlantic.add((cols - 1, y))

        for x in range(cols):
            pacific.add((x, 0))
            atlantic.add((x, rows - 1))
        
        queue = collections.deque()



        bfs(queue, atlantic)
        bfs(queue, pacific)

        print(atlantic)
        print(pacific)

        ans = []

        for x, y in atlantic:
            if (x, y) in pacific:
                ans.append([y, x])
        return ans







