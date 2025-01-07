class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, num in enumerate(nums):
            resid = target - num
            if resid in visited:
                return [i, visited[resid]]
            visited[num] = i

        
