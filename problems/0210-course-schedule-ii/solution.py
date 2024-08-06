class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            adjlist[prereq[1]].append(prereq[0])
        
        stack = []
        visited = [0] * numCourses

        def dfs(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True
            visited[node] = 1
            for course in adjlist[node]:
                if not dfs(course):
                    return False
            visited[node] = 2
            stack.append(node)
            return True
        
        for i in range(numCourses):
            if visited[i] == 2:
                continue
            if not dfs(i):
                return []

        return stack[::-1]
