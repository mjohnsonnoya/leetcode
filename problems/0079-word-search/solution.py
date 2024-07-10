class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j , index):
            if i >= len(board[0]) or i < 0 or j >= len(board) or j < 0 or board[j][i] != word[index]:
                return False
            if index == len(word) - 1:
                return True
            temp = board[j][i]
            board[j][i] = '#'
            for dx, dy in directions:
                if dfs(i + dx, j + dy, index + 1):
                    return True
            board[j][i] = temp
            return False

        

        for y in range(len(board)):
            for x in range(len(board[y])):
                if dfs(x,y,0):
                    return True
        return False
                
