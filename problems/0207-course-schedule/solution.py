from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Constructing the graph
        graph = {}
        for edge in prerequisites:
            if edge[1] in graph:
                graph[edge[1]].append(edge[0])
            else:
                graph[edge[1]] = [edge[0]]
        
        # 0: unvisited (white), 1: visiting (gray), 2: visited (black)
        visited = [0 for _ in range(numCourses)]
        
        def DFS(node):
            # If the node is not in graph, it does not prerequisite and hence, no cycle
            if node not in graph:
                return True
            
            # If the node is gray, cycle is found
            if visited[node] == 1:
                return False
            
            # If the node is black, no cycle found from this node
            if visited[node] == 2:
                return True
            
            # Mark the node as gray
            visited[node] = 1
            
            # Visit all neighbors
            for neighbor in graph[node]:
                if not DFS(neighbor):
                    return False
            
            # Mark the node as black
            visited[node] = 2
            return True
        
        # Running DFS for all nodes
        for i in range(numCourses):
            if not DFS(i):
                return False
        
        return True

