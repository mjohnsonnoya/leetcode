"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from queue import Queue
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
                return None
        mapping = {}
        
        queueBFS = Queue()
        queueBFS.put(node)
        
        mapping[node] = Node(node.val)
        
        while not queueBFS.empty():
                
                curr_node = queueBFS.get()
                
                for x in curr_node.neighbors:
                        if x not in mapping:
                                mapping[x] = Node(x.val)
                                queueBFS.put(x)
                        mapping[curr_node].neighbors.append(mapping[x])         
        return mapping[node]
