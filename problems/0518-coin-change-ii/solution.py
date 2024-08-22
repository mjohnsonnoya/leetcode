class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dfs(i, total):
            if total > amount:
                return 0
            if total == amount:
                return 1

            if (i, total) in cache:
                return cache[(i, total)]
            ways = 0
            for j in range(i, len(coins)):
                ways += dfs(j, total + coins[j])
            
            cache[(i, total)] = ways
            return ways
        return dfs(0, 0)
                

            
            
