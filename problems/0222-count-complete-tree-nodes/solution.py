# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional['TreeNode']) -> int:
        def left_depth(node):
            d = 0
            while node:
                d += 1
                node = node.left
            return d

        def right_depth(node):
            d = 0
            while node:
                d += 1
                node = node.right
            return d

        if not root:
            return 0

        ld = left_depth(root)
        rd = right_depth(root)
        if ld == rd:
            # perfect tree of height ld
            return (1 << ld) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

