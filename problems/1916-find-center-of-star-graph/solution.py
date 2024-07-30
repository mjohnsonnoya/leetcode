class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        nodetracker = set()
        for edge in edges:
            if edge[0]in nodetracker:
                return edge[0]
            elif edge[1] in nodetracker:
                return edge[1]
            else:
                nodetracker.add(edge[0])
                nodetracker.add(edge[1])
