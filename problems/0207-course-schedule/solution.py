from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            adjlist[prerequisite[1]].append(prerequisite[0])

        visited = set()
        checked = set()

        def dfs(i):
            if i in visited:
                return False
            if i in checked:
                return True

            visited.add(i)
            for neighbor in adjlist[i]:
                if not dfs(neighbor):
                    return False
            visited.remove(i)
            checked.add(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

