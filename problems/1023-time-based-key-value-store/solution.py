class TimeMap:

    def __init__(self):
        self.myDict = {}
    
    def __binarySearch(self, vals, timestamp):
        l, r = 0, len(vals) - 1
        res, idx = -1, -1
        while l <= r:
            m = l + (r - l)//2
            if vals[m][1] <= timestamp:
                if vals[m][1] >= res:
                    res = vals[m][1]
                    idx = m
                l = m + 1
            else:
                r = m - 1
        if idx != -1:
            # print(self.myDict)
            return vals[idx][0]
        else:
            return ""

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.myDict:
            self.myDict[key] = []
        self.myDict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.myDict:
            return ""
        else:
            return self.__binarySearch(self.myDict[key], timestamp)
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
