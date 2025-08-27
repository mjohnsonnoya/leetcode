class Solution {
public:
    std::unordered_map<int, int> dp{{}};
    int climbStairs(int n) {
        if (n == 1) return 1;
        if (n <= 0) return 0;
        if (n == 2) return 2;
        auto it = dp.find(n); if (it != dp.end()) return it->second;
        dp[n] = climbStairs(n - 1) + climbStairs(n - 2);
        return dp[n];
    }
};
