class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        cache = {}
        
        def helper(i, j, moves):
            if i < 0 or i >= n or j < 0 or j >= n:
                return 0
            if moves == k:
                return 1
            if (i, j, moves) in cache:
                return cache[(i, j, moves)]
            else:
                total = helper(i + 1, j + 2, moves + 1) + helper(i + 2, j + 1, moves + 1) + helper(i + 2, j - 1, moves + 1) + helper(i + 1, j - 2, moves + 1) + helper(i - 1, j - 2, moves + 1) + helper(i - 2, j - 1, moves + 1) + helper(i - 2, j + 1, moves + 1) + helper(i - 1, j + 2, moves + 1)
                cache[(i, j, moves)] = (1/8) * total
                return cache[(i, j, moves)]
        
        return helper(row, column, 0)
