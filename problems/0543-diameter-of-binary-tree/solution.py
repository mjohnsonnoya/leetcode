# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxdiameter = [0]
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            diam = 2 + left + right
            maxdiameter[0] = max(diam, maxdiameter[0])
            return 1 + max(left, right)
        dfs(root)
        return maxdiameter[0]
        
