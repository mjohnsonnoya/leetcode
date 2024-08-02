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
        visited = {}
        def dfs(i):
            visited[i] = Node(i.val)
            for neighbor in i.neighbors:
                if neighbor not in visited:
                    dfs(neighbor)
        if node:
            dfs(node)
        else:
            return node

        for k, v in visited.items():
            for neighbor in k.neighbors:
                v.neighbors.append(visited[neighbor])

        return visited[node]


