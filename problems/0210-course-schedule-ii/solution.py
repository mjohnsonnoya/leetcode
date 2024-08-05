class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            adjlist[prereq[1]].append(prereq[0])

        visited = [0] * numCourses
        stack = []
        def dfs(i):
            if visited[i] == 1:
                return False
            if visited[i] == 2:
                return True
            visited[i] = 1
            for course in adjlist[i]:
                 if not dfs(course):
                    return False
            visited[i] = 2
            stack.append(i)
            return True
        
        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return []
        
        return stack[::-1]
                
            


        
