class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            heapq.heappush(heap, (p[0]*p[0]+p[1]*p[1], p[0], p[1]))
        
        res = []
        while len(res) < k:
            _, x, y = heapq.heappop(heap)
            res.append([x, y])
        return res

