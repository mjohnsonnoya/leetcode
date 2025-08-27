class Solution {
public:
    int longestPalindrome(string s) {
        std::unordered_map<char, int> counts{};
        int length = 0;
        bool middle = false;

        for (char c : s) {
            counts[c] += 1;
        }
        for (auto [v, c] : counts) {
            if (c % 2 == 0) {
                length += c;
            }
            else {
                length += c - 1;
                middle = true;
            }
        }
        if (middle) {
            length += 1;
        }
        return length;
    }
};
