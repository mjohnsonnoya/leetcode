class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0, j = s.size() - 1;
        while (i < j) {
            while (i < j && !std::isalnum(s[i])) {
                ++i;
            }
            while (i < j && !std::isalnum(s[j])) {
                --j;
            }
            if (std::tolower(s[i]) != std::tolower(s[j])) {
                std::cout << s[i] << '\n';
                std::cout << s[j] << '\n';
                return false;
            }
            ++i;
            --j;
        }
        return true;
    }
};
