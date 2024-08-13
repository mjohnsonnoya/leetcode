class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 1, 2
        if n == 1:
            return 1
        for _ in range(2, n):
            tmp = second
            second = second + first
            first = tmp
        
        return second


