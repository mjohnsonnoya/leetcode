#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        // TODO(1): squared distance helper (use long long to avoid overflow)
        auto d2 = [](const vector<int>& p) -> long long {
            return 1LL * p[0] * p[0] + 1LL * p[1] * p[1];
        };

        // TODO(3): comparator that makes a max-heap by distance
        // (top() will be the farthest among the kept points)
        auto cmp = [&](const vector<int>& a, const vector<int>& b) {
            return d2(a) < d2(b);
        };

        // TODO(4): declare the heap with decltype(cmp) and pass cmp
        priority_queue<vector<int>, vector<vector<int>>, decltype(cmp)> heap(cmp);

        // ---- TODO(5): scan and maintain size-k heap
        if (k >= (int)points.size()) return points;  // quick edge case
        for (auto& p : points) {
            if ((int)heap.size() < k) {
                heap.push(p);
            } else if (d2(p) < d2(heap.top())) {  // new point is closer than current worst
                heap.pop();
                heap.push(p);
            }
        }

        // ---- TODO(6): build the answer from the heap
        vector<vector<int>> ans;
        ans.reserve(k);
        while (!heap.empty()) {
            ans.push_back(heap.top());  // order arbitrary
            heap.pop();
        }
        return ans;
    }
};

