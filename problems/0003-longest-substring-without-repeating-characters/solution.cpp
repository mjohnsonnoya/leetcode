class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0, r = 0;
        int maxlen = 0;
        std::unordered_set<char> seen;
        while (r < s.size()) {
            while (seen.contains(s[r])) {
                seen.erase(s[l]);
                l += 1;
            }
            maxlen = std::max(maxlen, r - l + 1);
            seen.insert(s[r]);
            r += 1;
        }
        return maxlen;
    }
};
