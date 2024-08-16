class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = [[] for _ in range(numCourses)]
        
        for prereq in prerequisites:
            adjlist[prereq[0]].append(prereq[1])

        visited = [0] * numCourses
        # cycle = [False]

        def dfs(course):
            if visited[course] == 2:
                return True
            if visited[course] == 1:
                # cycle[0] = True
                return False
            
            visited[course] = 1
            for c in adjlist[course]:
                if not dfs(c):
                    return False
            
            visited[course] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True


