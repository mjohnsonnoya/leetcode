class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda pair: (pair[0],-pair[1]))
        maxchain = 0
        dp = {}
        for i, pair in enumerate(pairs):
                j = i
                while True:
                        if pairs[j][1] < pairs[i][0]:
                                break
                        j -=1
                        if j == -1:
                                break
                if j == -1:
                        dp[i] = dp.get(i,0) +1
                        maxchain = max(maxchain, dp[i])
                else:
                        dp[i] = dp[j] + 1
                        maxchain = max(maxchain, dp[i])
        return maxchain
        
