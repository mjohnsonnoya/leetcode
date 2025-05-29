# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # consider a subtee rooted at r
        # we know that the diameter is longest path between any two nodes in the subtree rooted at r
        # therefore diamter(r) = max(diameter(r.left), diameter(r.right), 2 + maxdepth(r.left) + maxdepth(r.right))
        diameter = 0
        def helper(root):
            nonlocal diameter
            if not root:
                return -1
            l = helper(root.left)
            r = helper(root.right)

            diam = 2 + l + r
            diameter = max(diam, diameter)

            return 1 + max(l, r)
        
        helper(root)

        return diameter

            
