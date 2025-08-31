/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        int ans = 0;

        std::vector<std::pair<TreeNode*, int>> st{{root, 1}};
        while (!st.empty()) {
            auto [node, d] = st.back(); st.pop_back();
            ans = std::max(ans, d);

            if (node->left)  st.emplace_back(node->left,  1 + d);
            if (node->right) st.emplace_back(node->right, 1 + d);
    }
    return ans;

        
        
    }
};
