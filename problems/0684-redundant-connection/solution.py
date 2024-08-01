class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        rank = [1] * n
        parent = [i for i in range(1, n + 1)]

        def find(node):
            while parent[node - 1] != node:
                parent[node - 1] = parent[parent[node - 1] - 1]
                node = parent[node - 1]
            return node
        
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            if p1 == p2:
                return False
            
            if rank[p1 - 1] >= rank[p2 - 1]:
                parent[p2 - 1] = p1
                rank[p1 - 1] += rank[p2 - 1]
            
            else:
                parent[p1 - 1] = p2
                rank[p2 - 1] += rank[p1 - 1]
        
            return True
        
        for edge in edges:
            if not union(edge[0], edge[1]):
                return edge
            
