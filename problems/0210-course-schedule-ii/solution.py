class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            adjlist[prereq[1]].append(prereq[0])
        
        visited = [0] * numCourses
        has_cycle = [False]
        stack = []

        def dfs(node):
            if visited[node] == 1:
                has_cycle[0] = True
            if visited[node] == 2:
                return
            
            visited[node] = 1

            for course in adjlist[node]:
                if has_cycle[0]:
                    return
                dfs(course)
            visited[node] = 2
            stack.append(node)
        
        for node in range(numCourses):
            if not visited[node]:
                dfs(node)
                if has_cycle[0]:
                    return []
        return stack[::-1]
            

