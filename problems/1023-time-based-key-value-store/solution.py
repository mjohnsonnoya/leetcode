class TimeMap:

    def __init__(self):
        self.dictionary = {}
        
    def __binarySearch(self, vals, timestamp):
        l, r = 0, len(vals) - 1
        res = -1
        idx = -1
        while l <= r:
            m = l + (r - l)//2
            if vals[m][0] <= timestamp:
                if vals[m][0] >= res:
                    res = vals[m][0]
                    idx = m
                l = m + 1
            if vals[m][0] > timestamp:
                r = m - 1
        if idx == -1:
            return ""
        else:
            return vals[idx][1]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictionary:
            self.dictionary[key] = []
        self.dictionary[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dictionary:
            return ""
        return self.__binarySearch(self.dictionary[key],timestamp)


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
