class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::map<int, int> visited = {};
        for (int i = 0; i < nums.size(); i++) {
            int res = target - nums[i];
            if (visited.contains(res)) {
                return vector<int>{i, visited[res]};
            }
            else visited[nums[i]] = i;
        }
        return vector<int>{0, 0};
    }
};
