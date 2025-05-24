class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        buyprice = prices[0]
        for num in prices:
            if num < buyprice:
                buyprice = num
            else:
                maxprofit = max(maxprofit, num - buyprice)
        return maxprofit
