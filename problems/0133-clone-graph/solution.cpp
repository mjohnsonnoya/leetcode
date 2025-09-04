#include <unordered_map>
#include <deque>
#include <vector>
using namespace std;

/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() : val(0) {}
    Node(int _val) : val(_val) {}
    Node(int _val, vector<Node*> _neighbors) : val(_val), neighbors(_neighbors) {}
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        // TODO(1): handle empty input
        // if ( ... ) return ...;
        if (!node) return nullptr;

        // Map original -> clone
        unordered_map<Node*, Node*> mp;
        deque<Node*> q;
        q.emplace_back(node);
        mp[node] = new Node(node->val);

        // BFS
        while (!q.empty()) {
            Node* cur = q.front(); q.pop_front();

            for (Node* nei : cur->neighbors) {
                // TODO(3): if neighbor not cloned yet:
                if (!mp.contains(nei)) {
                    mp[nei] = new Node(nei->val);
                    q.emplace_back(nei);
                }

                // TODO(4): connect clones (add edge)
                mp[cur]->neighbors.push_back( mp[nei] );
            }
        }

        // TODO(5): return the clone corresponding to the input node
        return mp[node];
    }
};

