class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            adjlist[prereq[1]].append(prereq[0])
        
        print(adjlist)
        recstack = set()
        visited = set()

        def dfs(node):
            if node in recstack:
                return False
            if node in visited:
                return True
            recstack.add(node)
            for course in adjlist[node]:
                if not dfs(course):
                    return False
            recstack.discard(node)
            visited.add(node)
            return True
        
        for node in range(numCourses):
            if not dfs(node):
                return False
        return True
            

                

