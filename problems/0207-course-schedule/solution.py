class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            adjlist[prereq[0]].append(prereq[1])
        
        state = [0] * numCourses

        for course in range(numCourses):
            if state[course] != 0:
                continue
            stack = [(course, 0)]
            while stack:
                node, phase = stack.pop()
                if phase == 0:
                    if state[node] == 1:
                        return False
                    if state[node] == 2:
                        continue
                    state[node] = 1
                    stack.append((node, 1))
                    for nei in adjlist[node]:
                        stack.append((nei, 0))
                else: 
                    state[node] = 2
        
        return True
            



