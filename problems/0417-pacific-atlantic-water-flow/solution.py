class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        atlantic = set()
        pacific = set()
        ans = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = collections.deque()
        visited = set()
        for x in range(cols):
            visited.add((x, rows - 1))
            q.append((x, rows - 1))
        
        for y in range(rows):
            visited.add((cols - 1, y))
            q.append((cols - 1, y))
        
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                atlantic.add((x, y))
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx >= 0 and nx < cols and ny >= 0 and ny < rows and heights[ny][nx] >= heights[y][x] and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        q.append((nx, ny))

        visited = set()

        print(pacific)
        print(atlantic)

        for x in range(cols):
            visited.add((x, 0))
            q.append((x, 0))
        
        for y in range(rows):
            visited.add((0, y))
            q.append((0, y))

        
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                pacific.add((x, y))
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx >= 0 and nx < cols and ny >= 0 and ny < rows and heights[ny][nx] >= heights[y][x] and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        q.append((nx, ny))
        ans = []
        for y in range(rows):
            for x in range(cols):
                if (x, y) in pacific and (x, y) in atlantic:
                    ans.append([y, x])
    

        return ans
    
        

