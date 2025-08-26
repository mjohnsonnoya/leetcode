class Solution {
public:
    bool isValid(string s) {
        std::unordered_map<char,char> m{{'}','{'}, {')','('}, {']','['}};


        std::deque<char> q;
        auto it = s.begin();
        while (it != s.end()){
            if (q.empty()) {
                q.push_back(*it);
            }
            else { 
            if (auto search = m.find(*it); search != m.end() && search->second == q.back()) {
                q.pop_back();
            }else {
            q.push_back(*it);
            }
            }
            ++it;

        }
        return q.empty();
    }
};
