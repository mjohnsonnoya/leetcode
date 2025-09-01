class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> out;
        int i = 0, n = (int)intervals.size();

        // 1) add all intervals completely to the left of newInterval
        while (i < n && intervals[i][1] < newInterval[0]) {
            out.push_back(intervals[i++]);
        }

        // 2) merge all overlapping intervals into newInterval
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = min(newInterval[0], intervals[i][0]);
            newInterval[1] = max(newInterval[1], intervals[i][1]);
            ++i;
        }
        out.push_back(newInterval);

        // 3) add the rest
        while (i < n) out.push_back(intervals[i++]);

        return out;
    }
};

