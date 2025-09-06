# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # For each node I think we can generate condition for a valid range the node can take. For example left 
        # child of parent needs to be less than root. Right child of parent needs to be more than root
        def helper(root: Optional[TreeNode], vals) -> bool:
            if not root:
                return True
            if  not (vals[0] < root.val < vals[1]):
                return False
            
            return helper(root.left, [vals[0], root.val]) and helper(root.right, [root.val, vals[1]])
        
        return helper(root, [float('-inf'), float('inf')])
