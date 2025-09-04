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
    vector<vector<int>> levelOrder(TreeNode* root) {
        std::deque<TreeNode*> q;
        std::vector<std::vector<int>> ans {};

        if (!root) return ans;

        q.emplace_back(root);
        while (q.size() > 0) {
            int k = q.size();
            std::vector<int> level{};
            level.reserve(k);

            for (int dummy = 0; dummy < k; ++dummy) {
                TreeNode* node = q.front();
                if (node->left) {
                    q.emplace_back(node->left);
                }
                if (node->right) {
                    q.emplace_back(node->right);
                }
                level.emplace_back(node->val);
                q.pop_front();
            }
            ans.emplace_back(level);
        }
        return ans;
    }
};
