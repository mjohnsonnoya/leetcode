class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda word: len(word))
        maxChain = 1
        dp = {}
        dp[""] = 0
        for word in words:
            for i in range(len(word)):
                candidate = word[:i] + word[i + 1:]
                
                dp[word] = max(dp.get(word,0), dp.get(candidate, 0) + 1)
            maxChain = max(maxChain,dp[word])
        return maxChain
