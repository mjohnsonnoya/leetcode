class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        
        def dfs(i, state):
            if i >= len(prices):
                return 0
            if (i, state) in dp:
                return dp[(i,state)]
            
            cooldown = dfs(i + 1, state)
            if state:
                buying = dfs(i + 1, not state) - prices[i]
                dp[(i, state)] = max(buying, cooldown)
                
            else:
                selling = dfs(i + 2, not state) + prices[i]
                dp[(i,state)] = max(selling, cooldown)
                
            return dp[(i,state)]
        return dfs(0, True)
