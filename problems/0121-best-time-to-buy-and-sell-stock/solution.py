class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        high = 0
        maxprofit = 0
        for price in prices:
            if price < low:
                low = price
                high = price
            if price > high:
                high = price
            maxprofit = max(maxprofit, high - low)
        return maxprofit
