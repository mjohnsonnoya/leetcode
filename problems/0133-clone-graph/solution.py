"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        mapping = {}
        q = deque([])
        q.append(node)
        while q:
            vertex = q.popleft()
            mapping[vertex] = Node(val = vertex.val)

            for neighbor in vertex.neighbors:
                if neighbor not in mapping:
                    q.append(neighbor)
        
        for key in mapping.keys():
            mapping[key].neighbors = [mapping[neighbor] for neighbor in key.neighbors]
        
        return mapping[node]
        
