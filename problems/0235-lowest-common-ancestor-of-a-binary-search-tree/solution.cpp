/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        std::function<TreeNode*(TreeNode*)> dfs = [&](TreeNode* node) -> TreeNode* {
            if (!node) return nullptr;

            if (node == p) return node;
            if (node == q) return node;

            TreeNode* left = dfs(node -> left);
            TreeNode* right = dfs(node -> right);

            if (left && right) return node;

            return left ? left : right;

        };
        return dfs(root);
    }
};
