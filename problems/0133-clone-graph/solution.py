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
        nodemap = {}
        nodemap[node] = Node(val=node.val)

        q = deque()
        q.append(node)
        while q:
            vertex = q.popleft()
            for neighbor in vertex.neighbors:
                if neighbor not in nodemap:
                    nodemap[neighbor] = Node(val=neighbor.val)
                    q.append(neighbor)
                nodemap[vertex].neighbors.append(nodemap[neighbor])

        
        return nodemap[node]
        
