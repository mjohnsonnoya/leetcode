class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        res = []
        currstart,currend = intervals[0][0],intervals[0][1]
        
        def overlap(interval1,interval2):
                if (interval2[0] <= interval1[0] <= interval2[1]) or (interval2[0] <= interval1[1] <= interval2[1]):
                        return True
                
                elif (interval1[0] <= interval2[0] <= interval1[1]) or (interval1[0] <= interval2[1] <= interval1[1]):
                        return True
                
                else:
                        return False
                
        for i in range(len(intervals)):
                if overlap([currstart,currend],intervals[i]): 
                        currstart = min(currstart,intervals[i][0])
                        currend = max(currend,intervals[i][1])
                else:
                        res.append([currstart,currend])
                        currstart,currend = intervals[i][0],intervals[i][1]
        res.append([currstart,currend])
        return res
