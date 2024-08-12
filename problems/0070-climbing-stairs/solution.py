class Solution:
    def climbStairs(self, n: int) -> int:
        i1, i2 = 1, 1
        for i in range(2, n + 1):
            temp = i1
            i1 = i2
            i2 = temp + i2
        return i2

        
