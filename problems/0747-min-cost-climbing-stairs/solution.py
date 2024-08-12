class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        if len(cost) == 1:
            return cost[0]
        
        first = cost[0]
        second = cost[1]
        n = len(cost)
        for i in range(2, n):
            current = cost[i] + min(first, second)
            first = second
            second = current
        return min(first, second)
