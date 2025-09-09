from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency: a -> b means "a depends on b"
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[a].append(b)

        # 0 = unvisited, 1 = visiting, 2 = done
        state = [0] * numCourses

        for start in range(numCourses):
            if state[start] != 0:
                continue

            stack = [(start, 0)]  # (node, phase), phase 0=pre, 1=post
            while stack:
                node, phase = stack[-1]

                if phase == 0:
                    # If we're about to visit a node currently on the path -> cycle
                    if state[node] == 1:
                        return False  # back-edge found

                    # If already fully processed, nothing to do
                    if state[node] == 2:
                        stack.pop()
                        continue

                    # Mark as visiting and schedule post-phase
                    state[node] = 1                                    # <-- fill (set visiting)
                    stack[-1] = (node, 1)                              # <-- fill (flip to post)

                    # Explore neighbors (dependencies)
                    for nei in adj[node]:
                        if state[nei] == 0:                            # <-- fill (only push unvisited)
                            stack.append((nei, 0))

                        elif state[nei] == 1:
                            # Neighbor on the path -> cycle
                            return False

                else:
                    # Post-phase: mark done and pop
                    state[node] = 2                                    # <-- fill (set done)
                    stack.pop()

        return True

