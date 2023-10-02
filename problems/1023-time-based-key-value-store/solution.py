class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
                self.data[key] = []
        self.data[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
                return ""
        values = self.data[key]
        l, r = 0, len(values) - 1
        while l <= r:
                m = (l + r)//2
                if values[m][1] == timestamp:
                        return values[m][0]
                elif values[m][1] > timestamp:
                        r = m -1
                else:
                        l = m + 1
        if r >= 0:
                return values[r][0]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
