class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # new interval
        # for each interval before that doesn't overlap with nI_start add it.
        # if overlap add keep iterating over all the intervals that overlap and return min start of all the intervals and max start
        # add all the intervals that don't overlap
        
        newIntervals = []
        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                newIntervals.append(interval)
            elif interval[0] > newInterval[1]:
                newIntervals.append(newInterval)
                return newIntervals + intervals[i:]
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
        
        newIntervals.append(newInterval)
        return newIntervals


            


