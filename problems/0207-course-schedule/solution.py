class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            adj[prereq[0]].append(prereq[1])
        
        state = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited

        for course in range(numCourses):
            if state[course] != 0:  
                continue  # already processed
            
            stack = [(course, 0)]
            while stack:
                node, phase = stack[-1]

                if phase == 0:
                    state[node] = 1
                    stack[-1] = (node, 1)
                    for nei in adj[node]:
                        if state[nei] == 1:
                            return False  # cycle
                        if state[nei] == 0:
                            stack.append((nei, 0))

                else:  # exit phase
                    state[node] = 2
                    stack.pop()

        return True

