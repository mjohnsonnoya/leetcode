# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
                return []
        
        my_queue = Queue()
        my_queue.put(root)
        vals = []
        
        while not my_queue.empty():
                level_size = my_queue.qsize()
                current_level = []
                for _ in range(level_size):
                        
                        node = my_queue.get()
                        current_level.append(node.val)
                        
                        
                        if node.left:
                                my_queue.put(node.left)
                        if node.right:
                                my_queue.put(node.right)
                vals.append(current_level)                  
        return vals
                
