class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0
        s = 0
        maxprof = 0
        while s < (len(prices)):
            if (prices[s] - prices[b]) < 0:
                b = s
            if (prices[s] - prices[b]) > maxprof:
                maxprof = prices[s] - prices[b]
            s = s + 1
        return maxprof

