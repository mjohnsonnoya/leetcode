class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        rank = [1] * n
        parent = [i for i in range(n)]

        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            
            return node
        
        def union(node1, node2):
            pn1 = find(node1)
            pn2 = find(node2)
            if pn1 == pn2:
                return False
            if rank[pn1] >= rank[pn2]:
                parent[pn2] = pn1
                rank[pn1] += rank[pn2]
            else:
                parent[pn1] = pn2
                rank[pn2] += rank[pn1]
            return True
        
        for edge in edges:
            if not union(edge[0] - 1, edge[1] - 1):
                return edge

        


