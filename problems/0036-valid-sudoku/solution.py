class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        def isValidRow(i):
            nums = set()
            for num in board[i]:
                if num in nums:
                    return False
                else:
                    if num != ".":
                        nums.add(num)
            return True
        
        def isValidCol(j):
            z = 0
            nums = set()
            while z < len(board):
                if board[z][j] in nums:
                    print(nums)
                    return False
                else:
                    if board[z][j] != ".":
                        nums.add(board[z][j])
                z += 1
            return True
        
        def isValidBox(i, j):
            c = i + 3
            d = j + 3
            nums = set()
            while i < c:
                while j < d:
                    if board[i][j] in nums:
                        return False
                    else:
                        if board[i][j] != ".":
                            nums.add(board[i][j])
                    j += 1
                j -= 3
                i += 1
            return True
        
        for i in range(len(board)):
            if not isValidRow(i):
                print("valrow trigger")
                return False
            if not isValidCol(i):
                print("valcol trigger")
                return False
        
        x = [0, 3, 6]
        y = [0, 3, 6]

        for i in x:
            for j in y:
                if not isValidBox(i, j):
                    print("valbox trigger")
                    return False
        
        return True





