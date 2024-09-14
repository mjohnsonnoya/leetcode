class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        print(parent)

        def find(node):
            dummy = node
            while parent[dummy] != dummy:
                dummy = parent[dummy]
            
            while node != dummy:
                next_n = parent[node]
                parent[node] = dummy
                node = next_n
            return dummy
        
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if root1 == root2:
                return False
            parent[root1] = root2  # Union by assigning one root to the other
            return True

        
        for x, y in edges:
            if not union(x, y):
                return [x, y]
        
            


        # def union()
        # def find()

