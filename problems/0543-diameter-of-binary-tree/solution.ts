/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function diameterOfBinaryTree(root: TreeNode | null): number {
    // diameter of Binary tree at root is equal to max diameter of tree rooted at root.left or root.right, or it could be 2 + depth(root.left) + depth(root.right)


    function helper(root: TreeNode | null): [number, number] {
        if (!root) {
            return [0, -1];
        }

        const [leftDiam, leftDepth] = helper(root.left);
        const [rightDiam, rightDepth] = helper(root.right);

        return [Math.max(2 + leftDepth + rightDepth, leftDiam, rightDiam), 1 + Math.max(leftDepth, rightDepth)];
    }

    const [diam, depth] = helper(root);

    return diam;


};
