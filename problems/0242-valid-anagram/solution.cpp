#include <unordered_map>
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;

        std::unordered_map<char, int> freq{};
        for (char& c : s) {
            freq[c] += 1;
        }

        for (char& c : t) {
            if (!freq.contains(c)) {
                return false;
            }
            --freq[c];
            if (freq[c] == 0){
                freq.erase(c);
            }
        }
        return freq.empty();
    };
};
