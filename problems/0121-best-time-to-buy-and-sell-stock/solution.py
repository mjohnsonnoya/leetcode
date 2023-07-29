class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0
        s = 0
        maxprof = 0
        while s <= (len(prices) - 1):
            maxprof = max(maxprof,prices[s] - prices[b])
            if prices[s] - prices[b] < 0:
                b = s
            else:
                s +=1 
        return maxprof

