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
    let maxDiameter = 0;

    function depth(root: TreeNode | null): number {
        if (!root) {
            return -1;
        }

        const leftDepth = depth(root.left);
        const rightDepth = depth(root.right);

        maxDiameter = Math.max(maxDiameter, 2 + leftDepth + rightDepth);

        return 1 + Math.max(leftDepth, rightDepth);
    }

    depth(root);

    return maxDiameter;
};
