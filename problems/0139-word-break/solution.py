class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s))

        for i in range(len(s)):
            if s[:i+1] in wordDict:
                dp[i] = True
            for word in wordDict:
                if i < len(word) - 1:
                    continue
                if dp[i - len(word)] and s[i+1 - len(word):i+1] == word:
                    dp[i] = True
        
        print(dp)
        return dp[len(s) - 1]
