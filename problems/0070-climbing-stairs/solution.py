class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def calculate_fibonacci(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            
            if n in dp:
                return dp[n]
            
            dp[n] = calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)
            return dp[n]
        
        return calculate_fibonacci(n)

