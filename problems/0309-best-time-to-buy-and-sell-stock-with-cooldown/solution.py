class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        n = len(prices) - 1

        def helper(i, state):
            if i > n:
                return 0

            if (i, state) in cache:
                return cache[(i, state)]
            
            if state:
                ans = max(helper(i + 1, not state) - prices[i], helper(i + 1, state))
                cache[(i, state)] = ans
                return ans
            else:
                ans = max(helper(i + 2, not state) + prices[i], helper(i + 1, state))
                cache[(i, state)] = ans
                return ans
        
        return helper(0, True)
