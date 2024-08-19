class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0  # No jumps needed if there's only one element
        
        queue = deque([0])  # Start BFS from the first index
        visited = set([0])  # To avoid processing an index more than once
        steps = 0
        
        while queue:
            size = len(queue)
            for _ in range(size):
                idx = queue.popleft()
                
                # If the farthest point from this index reaches or exceeds the last index, return the count
                if idx + nums[idx] >= len(nums) - 1:
                    return steps + 1
                
                # Add new indices to the queue, which are within reach from the current index
                for i in range(idx + 1, idx + nums[idx] + 1):
                    if i not in visited:
                        visited.add(i)
                        queue.append(i)
                        
            steps += 1
        
        return steps
        
