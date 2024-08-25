class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s2) + len(s1):
            return False
        
        if not s2:
            return s1 == s3
        
        if not s1:
            return s2 == s3
        
        n = len(s1)
        m = len(s2)

        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True

        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s2[i - 1] == s3[i - 1]
        
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s1[j - 1] == s3[j - 1]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s3[i + j - 1] == s2[i - 1] and dp[i - 1][j]:
                    dp[i][j] = True
                elif s3[i + j - 1] == s1[j - 1] and dp[i][j - 1]:
                    dp[i][j] = True
        
        return dp[m][n]



        

