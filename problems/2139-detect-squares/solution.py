class DetectSquares:

    def __init__(self):
        self.counts = {}
        self.points = []
        

    def add(self, point: List[int]) -> None:
        self.points.append(tuple(point))
        if tuple(point) in self.counts:
            self.counts[tuple(point)] += 1
        else:
            self.counts[tuple(point)] = 1
        

    def count(self, point: List[int]) -> int:
        px, py = point
        ans = 0
        for x, y in self.points:
            if ((px - x)**2  == (py - y)**2) and (px != x and py != y):
                if (px, y) in self.counts and (x, py) in self.counts:
                    ans += self.counts[(px, y)] * self.counts[(x, py)]
        
        return ans




# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
