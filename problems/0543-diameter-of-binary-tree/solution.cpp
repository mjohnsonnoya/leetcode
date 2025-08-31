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
    static int dfs(TreeNode* node, int& best) {
        if (!node) return 0;                  // height of null = 0
        int l = dfs(node->left,  best);
        int r = dfs(node->right, best);
        best = std::max(best, l + r);         // diameter in edges
        return 1 + (l > r ? l : r);
    }
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int best = 0;
        dfs(root, best);
        return best;
    }
};

