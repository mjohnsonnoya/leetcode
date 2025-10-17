#include <unordered_map>
#include <stack>
#include <string>
class Solution {
public:
    bool isValid(string s) {
        std::unordered_map<char, char> m = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };
        std::stack<char> st;
        for (char& c : s) {
            if (c == '(' || c == '[' || c == '{') {
                st.push(c);
            }
            else {
                if (st.empty() || st.top() != m[c]) {
                    return false;
                }
                st.pop();
            }
        }
        return st.empty();
    }
};
