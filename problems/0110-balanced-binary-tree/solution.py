# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _balanced = True
        def helper(root):
            nonlocal _balanced
            if not root:
                return 0
            lh = helper(root.left)
            rh = helper(root.right)
            
            if not (1 >= (rh - lh) >=-1):
                _balanced = False

            return 1 + max(lh, rh)
        
        helper(root)
        return _balanced
        


        
