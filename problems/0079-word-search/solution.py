class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        rows, cols = len(board), len(board[0])

        def dfs(x, y, index):
            if index == len(word):
                return True
            if x < 0 or x >= cols or y < 0 or y >= rows or board[y][x] != word[index]:
                return False
            
            # Mark the current cell as visited
            temp = board[y][x]
            board[y][x] = '#'
            
            # Explore all possible directions
            found = (dfs(x + 1, y, index + 1) or
                     dfs(x - 1, y, index + 1) or
                     dfs(x, y + 1, index + 1) or
                     dfs(x, y - 1, index + 1))
            
            # Restore the current cell
            board[y][x] = temp
            
            return found
        
        for y in range(rows):
            for x in range(cols):
                if board[y][x] == word[0] and dfs(x, y, 0):
                    return True
        
        return False

