# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if not node:
                pass
            else:
                left, right = node.left, node.right
                node.left = right
                helper(node.left)
                node.right = left
                helper(node.right)
        helper(root)
        return root
