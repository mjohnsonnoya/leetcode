class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int cur = nums[0];
        int best = nums[0];
        for (int i = 1; i < (int)nums.size(); ++i) {
            cur = std::max(cur + nums[i], nums[i]);
            best = std::max(cur, best); 
        }
        return best;
    }
};
