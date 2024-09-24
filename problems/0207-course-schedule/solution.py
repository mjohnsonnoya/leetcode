class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            adjlist[prereq[1]].append(prereq[0])
        
        visited = [0] * numCourses

        def dfs(course):
            # nonlocal visited
            if visited[course] == 1:
                return False
            if visited[course] == 2:
                return True
            
            visited[course] = 1
            for node in adjlist[course]:
                if not dfs(node):
                    return False
            
            visited[course] = 2
            return True
        
        for node in range(numCourses):
            if visited[node] == 2:
                continue
            if not dfs(node):
                return False
            
        return True
