class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        seen = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(x, y, i):
            if i == len(word):
                return True
            
            if not(0 <= x < cols and 0 <= y < rows and board[y][x] == word[i] and (x, y) not in visited):
                return False

            visited.add((x, y))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if dfs(nx, ny, i + 1):
                    return True

            visited.discard((x, y))
            return False


            

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    visited = set()
                    if dfs(col, row, 0):
                        return True
            
        return False
    
