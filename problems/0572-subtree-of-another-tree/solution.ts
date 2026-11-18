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

function isSubtree(root: TreeNode | null, subRoot: TreeNode | null): boolean {
    if (!root || !subRoot) {
        return !root && !subRoot;
    }
    function isSametree(p: TreeNode | null, q: TreeNode | null): boolean {
        if (!p || !q) {
            return !p && !q;
        }

        return (p.val === q.val && isSametree(p.left, q.left) && isSametree(p.right, q.right))
    }

    return isSametree(root, subRoot) || isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
};
