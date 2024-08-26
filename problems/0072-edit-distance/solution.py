class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # if word1 = "" and word2 = "abcdef":
            # edit distaances = len(word2)
        # if word1 == word2: ops = 0
        # rows = (len(word1) + 1)
        # cols = (len(word2) + 1)
        # dp[i][j] = f(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + 0 if word1[i] == word2[j] or + 1)
        
        rows = len(word1) + 1
        cols = len(word2) + 1
        dp = [[0] * cols for _ in range(rows)]
        
        for i in range(rows):
            dp[i][0] = i
        
        for j in range(cols):
            dp[0][j] = j
        
        for i in range(1, rows):
            for j in range(1, cols):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j] + 1, dp[i][j - 1] + 1)
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1)
        
        return dp[rows - 1][cols - 1]

