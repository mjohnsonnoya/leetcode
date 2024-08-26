class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        
        l, r = 0, 0
        tank = 0
        while r < len(gas) and l < len(gas):
            if tank < 0:
                l = r
                tank = 0
            tank += (gas[r] - cost[r])
            r += 1
        
        if tank >= 0:
            return l
        else:
            return -1
            


