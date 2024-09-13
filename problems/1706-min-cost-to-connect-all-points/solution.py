import math
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []
        n = len(points)
        in_mst = set()
        dist = [float('inf')] * n
        heapq.heappush(heap, (0, points[0]))
        
        ans = 0
        while heap:
            dist, point = heapq.heappop(heap)

            if tuple(point) in in_mst:
                continue
            
            in_mst.add(tuple(point))

            ans += dist

            for p2 in points:
                if not tuple(p2) in in_mst:
                    mdist = abs(point[0]-p2[0]) + abs(point[1]-p2[1])
                    heapq.heappush(heap, (mdist, p2))
        
        return ans

