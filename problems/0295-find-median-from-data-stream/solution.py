import heapq
class MedianFinder:

    def __init__(self):
        self.smallest = []
        self.biggest = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallest,-1 * num)
        sizedif = len(self.smallest) - len(self.biggest)
        if sizedif > 1:
            val = heapq.heappop(self.smallest)
            heapq.heappush(self.biggest,-1 * val)
        elif sizedif < -1:
            val = heapq.heappop(self.biggest)
            heapq.heappush(self.smallest,-1 * val)
        if self.smallest and self.biggest and -1 * self.smallest[0] > self.biggest[0]:
            val = heapq.heappop(self.smallest)
            heapq.heappush(self.biggest, -1 * val)
        sizedif = len(self.smallest) - len(self.biggest)
        if sizedif > 1:
            val = heapq.heappop(self.smallest)
            heapq.heappush(self.biggest,-1 * val)
        elif sizedif < -1:
            val = heapq.heappop(self.biggest)
            heapq.heappush(self.smallest,-1 * val)
    def findMedian(self) -> float:
        # heap has even number of elements
        if len(self.smallest) == len(self.biggest):
            return (-1 * self.smallest[0] + self.biggest[0])/2
        elif len(self.smallest) > len(self.biggest):
            return -1 * self.smallest[0]
        else:
            return self.biggest[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
