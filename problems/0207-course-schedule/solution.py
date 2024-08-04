class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = [[] for _ in range(numCourses)]

        for prereq in prerequisites:
            adjlist[prereq[1]].append(prereq[0])
        
        visited = [0] * numCourses
        cycle = [False]

        def dfs(i):
            if i in stack:
                print("i: ", i)
                print("stack: ", stack)
                cycle[0] = True
                return
            if visited[i] == 1:
                return
            stack.add(i)
            for course in adjlist[i]:
                dfs(course)
                if cycle[0]:
                    return
            stack.discard(i)
            visited[i] = 1

        for i in range(numCourses):
            stack = set()
            dfs(i)
            if cycle[0]:
                return False
        
        return True

