#include <vector>
#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> res;
        for (size_t i = 0; i < nums.size(); ++i) {
            int num = nums[i];
            int diff = target - num;
            if (res.contains(diff)) {
                return {res[diff], static_cast<int>(i)};
            }
            else {
                res[num] = static_cast<int>(i);
            }
        }
        return {};
    }
};
