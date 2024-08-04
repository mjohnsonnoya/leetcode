class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        rows = len(board)
        cols = len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(x, y):
            visited.add((x, y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0<=nx<cols and 0<=ny<rows and board[ny][nx] == "O" and (nx, ny) not in visited:
                    dfs(nx, ny)
        
        for y in range(rows):
            if board[y][0] == "O":
                dfs(0, y)
            if board[y][cols - 1] == "O":
                dfs(cols - 1, y)
        
        for x in range(cols):
            if board[0][x] == "O":
                dfs(x, 0)
            if board[rows - 1][x] == "O":
                dfs(x, rows - 1)
        
        for y in range(rows):
            for x in range(cols):
                if (x, y) not in visited:
                    board[y][x] = "X"
                    


