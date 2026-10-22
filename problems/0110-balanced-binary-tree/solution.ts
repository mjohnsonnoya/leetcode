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

function isBalanced(root: TreeNode | null): boolean {
    let balanced = true;

    function depth(root: TreeNode | null): number {
        if (!root) {
            return 0;
        }

        const leftDepth = depth(root.left);
        const rightDepth = depth(root.right);

        if (Math.abs(leftDepth - rightDepth) > 1) {
            balanced = false;
        }


        return 1 + Math.max(leftDepth, rightDepth);
    }

    depth(root);

    return balanced;
};
