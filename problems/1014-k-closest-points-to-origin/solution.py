import heapq
import math
from typing import List

class Solution:
    
    def squaredDistance(self, point1, point2):
        return sum((point1[i] - point2[i])**2 for i in range(len(point1)))
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for point in points:
            distance = self.squaredDistance(point, [0, 0])
            heapq.heappush(heap, (-distance, point))
            
            if len(heap) > k:
                heapq.heappop(heap)
            
        return [item[1] for item in heap]

