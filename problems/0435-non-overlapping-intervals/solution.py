class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])

        curr_interval = intervals[0]
        ans = 0
        for i in range(1, len(intervals)):
            if curr_interval[1] <= intervals[i][0]:
                curr_interval = intervals[i]
            else:
                ans += 1
                if curr_interval[1] > intervals[i][1]:
                    curr_interval = intervals[i]

        return ans


