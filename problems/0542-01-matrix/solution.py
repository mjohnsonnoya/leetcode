class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        visited = set()
        numrows, numcols = len(mat), len(mat[0])
        for r in range(numrows):
            for c in range(numcols):
                if mat[r][c] == 0:
                    visited.add((r, c))
                    q.append((r, c))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        val = 0
        while q:
            m = len(q)
            for _ in range(m):
                r,c = q.popleft()
                mat[r][c] = val
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < numrows and 0 <= nc < numcols and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))
            val += 1
        
        return mat

