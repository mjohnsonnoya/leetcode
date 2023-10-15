class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        
        dp = [[float('inf') for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        
        dp[len(s1)][len(s2)] = 0
        for i in range(len(s1) - 1, -1, -1):
            dp[i][len(s2)] = ord(s1[i]) + dp[i + 1][len(s2)]
        for j in range(len(s2) - 1, -1, -1):
            dp[len(s1)][j] = ord(s2[j]) + dp[len(s1)][j + 1]
            
        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s2) - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(ord(s1[i]) + dp[i + 1][j], ord(s2[j]) + dp[i][j + 1])
        return dp[0][0]
