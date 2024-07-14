class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            y = -1 * heapq.heappop(stones)
            x = -1 * heapq.heappop(stones)
            if y - x == 0:
                continue
            else:
                heapq.heappush(stones, -1 * (y - x))
        if len(stones) == 0:
            return 0
        else:
            return -1 * stones[0]
