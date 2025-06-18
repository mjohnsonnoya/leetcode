class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            adjlist[prereq[0]].append(prereq[1])
        
        state = [0] * numCourses

        for course in range(numCourses):
            if state[course] != 0:
                continue
            
            stack = []
            path = set()
            stack.append(course)

            while stack:
                curr = stack[-1]
                if state[curr] == 2:
                    stack.pop()
                    continue

                if curr in path:
                    stack.pop()
                    state[curr] = 2
                    path.remove(curr)
                    continue
                
                path.add(curr)
                has_unvisited = False
                for neighbor in adjlist[curr]:
                    if state[neighbor] == 1 or neighbor in path:
                        return False
                    if state[neighbor] == 0:
                        stack.append(neighbor)
                        has_unvisited = True
                
                if not has_unvisited:
                    stack.pop()
                    state[curr] = 2
                    path.remove(curr)
            
        return True
