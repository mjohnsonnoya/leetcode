class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            adjlist[prereq[0]].append(prereq[1])

        visited = [0] * numCourses
        ans = []
        def dfs(course):
            if visited[course] == 1:
                return False
            
            if visited[course] == 2:
                return True
            
            visited[course] = 1
            for node in adjlist[course]:
                if not dfs(node):
                    return False
            
            visited[course] = 2
            ans.append(course)
            return True
        
        for node in range(numCourses):
            if not dfs(node):
                return []
        
        return ans


            
            
            



            
