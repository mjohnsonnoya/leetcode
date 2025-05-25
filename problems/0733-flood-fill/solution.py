class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        def BFS(sr, sc):
            queue = deque()
            queue.append((sr, sc))
            original = image[sr][sc]
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            while queue:
                r, c = queue.popleft()
                image[r][c] = color
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == original:
                        queue.append((nr, nc))
        if image[sr][sc] == color:
            return image
        BFS(sr, sc)
        return image





