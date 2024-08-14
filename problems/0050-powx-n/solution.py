class Solution:
    def myPow(self, x: float, n: int) -> float:
        dp = {}
        def helper(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            if n == -1:
                return 1/x
            if n in dp:
                return dp[n]
            if not n % 2:
                ans = helper(x, n // 2) * helper(x, n // 2)
                dp[n] = ans
                return ans
            else:
                ans = x * helper(x, n // 2) * helper(x, n // 2)
                dp[n] = ans
                return ans
        
        return helper(x, n)
        
