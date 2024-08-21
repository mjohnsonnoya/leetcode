class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1
        
        for i in range(i, len(intervals)):
            if not (newInterval[0] > intervals[i][1] or newInterval[1] < intervals[i][0]):
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            else:
                return ans + [newInterval] + intervals[i:]

        return ans + [newInterval]
