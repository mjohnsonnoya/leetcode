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
        nodes = {node: Node(val=node.val)}
        q = deque([node])
        while q:
            vertex = q.popleft()
            nodes[vertex] = Node(val=vertex.val)
            for neighbor in vertex.neighbors:
                if neighbor not in nodes:
                    q.append(neighbor)
        
        for key, val in nodes.items():
            for neighbor in key.neighbors:
                val.neighbors.append(nodes[neighbor])
        
        return nodes[node]


