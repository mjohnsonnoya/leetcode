class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])

        ans = []
        curr = intervals[0]
        for i in range(1, len(intervals)):
            if curr[1] < intervals[i][0]:
                ans.append(curr)
                curr = intervals[i]
            else:
                curr = [min(curr[0], intervals[i][0]), max(curr[1], intervals[i][1])]
        
        ans.append(curr)
        return ans


        
