# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        cache = {}
        
        def dfs(node):
            if not node:
                return 0
            if node in cache:
                return cache[node]
            cache[node] = node.val + dfs(node.left) + dfs(node.right)
            return cache[node]
        
        dfs(root)
        
        total_sum = cache[root]
        maxproduct = 0
        
        # myqueue = [root]
        # while myqueue:
        #     node = myqueue.pop(0)
        #     maxproduct = max(maxproduct, (total_sum - cache[node]) * cache[node])
        #     if node.left:
        #         myqueue.append(node.left)
        #     if node.right:
        #         myqueue.append(node.right)
        
        def search(node):
            nonlocal maxproduct
            if not node:
                return
            maxproduct = max(maxproduct, (total_sum - cache[node]) * cache[node])
            search(node.left)
            search(node.right)
        
        search(root)
        
        return maxproduct % (10**9 + 7) 
