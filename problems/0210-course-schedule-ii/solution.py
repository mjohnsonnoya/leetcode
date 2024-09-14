class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = defaultdict(list)
        for a, b in prerequisites:
            adjlist[a].append(b)
    
        path = []
        visited = [0] * numCourses
        def dfs(course):
            if visited[course] == 1:
                return False
            if visited[course] == 2:
                return True

            visited[course] = 1
            for i in range(len(adjlist[course])):
                if not dfs(adjlist[course][i]):
                    return False

            visited[course] = 2
            path.append(course)
            return True


        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return path
            
            
            



            
