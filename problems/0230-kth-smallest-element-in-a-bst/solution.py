# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        self.node_val = None
        def inorder(root):
            if not root or self.node_val:
                return
            inorder(root.left)
            self.count -= 1
            if self.count == 0:
                self.node_val = root.val
            inorder(root.right)
        inorder(root)
        return self.node_val

