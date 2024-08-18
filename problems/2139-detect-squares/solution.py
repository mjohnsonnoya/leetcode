class DetectSquares:

    def __init__(self):
        self.counts = {}
        
    def add(self, point: List[int]) -> None:
        if tuple(point) in self.counts:
            self.counts[tuple(point)] += 1
        else:
            self.counts[tuple(point)] = 1

    def count(self, point: List[int]) -> int:
        ans = 0
        for key, val in self.counts.items():
            if (((key[1] - point[1])**2) == ((key[0] - point[0])**2) and (key[1] != point[1]) and (key[0] != point[0])):

                if (key[0], point[1]) in self.counts and (point[0], key[1]) in self.counts:
                    ans += val * self.counts[(key[0], point[1])] * self.counts[(point[0], key[1])]
        return ans

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
