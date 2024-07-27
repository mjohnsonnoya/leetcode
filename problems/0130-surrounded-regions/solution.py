class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0,1),(0, -1), (1, 0), (-1, 0)]
        visited = set()
        rows = len(board)
        cols = len(board[0])

        def dfs(x, y):
            visited.add((x, y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < cols and ny >= 0 and ny < rows and board[ny][nx] == "O" and (nx, ny) not in visited:
                    dfs(nx, ny)
        
        for x in range(cols):
            if board[0][x] == 'O':
                dfs(x, 0)
            if board[rows - 1][x] == 'O':
                dfs(x, rows - 1)
        
        for y in range(rows):
            if board[y][0] == 'O':
                dfs(0, y)
            if board[y][cols - 1] == 'O':
                dfs(cols - 1, y)

        for y in range(rows):
            for x in range(cols):
                if (x, y) not in visited:
                    board[y][x] = "X"

