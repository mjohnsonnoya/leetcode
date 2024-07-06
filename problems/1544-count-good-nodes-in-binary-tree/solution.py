# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(root, maxval):
            if not root:
                return
            print ("root val: ",root.val)
            print("maxval: ",maxval)
            nonlocal count
            if root.val >= maxval:
                count += 1
                maxval = root.val
            dfs(root.left, maxval)
            dfs(root.right, maxval)
        dfs(root, root.val)

        return count

