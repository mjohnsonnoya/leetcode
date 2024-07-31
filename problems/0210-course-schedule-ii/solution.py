class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            adjlist[prereq[1]].append(prereq[0])

        visited = [0] * numCourses
        cycle = [False]
        stack = []
        def dfs(node):
            if visited[node] == 1:
                 cycle[0] = True
                 return
            if visited[node] == 2:
                return

            visited[node] = 1
            for course in adjlist[node]:
                dfs(course)
                if cycle[0]:
                    return
            
            visited[node] = 2
            stack.append(node)
            return

        for i in range(numCourses):
            dfs(i)
            if cycle[0]:
                return []
        
        return stack[::-1]

