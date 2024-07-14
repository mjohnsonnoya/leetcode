class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            heap.append((point[0] * point[0] + point[1] * point[1], point[0], point[1]))

        heapq.heapify(heap)
        ans = []
        while k > 0:
            ans.append(heapq.heappop(heap)[1:])
            k -= 1
        return ans
