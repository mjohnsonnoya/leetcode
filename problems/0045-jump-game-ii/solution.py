class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        r = 0
        farthest = 0
        steps = 0
        while r < len(nums):
            print(farthest)
            for i in range(r, min(farthest + 1, len(nums))):
                farthest = max(farthest, nums[i] + i)
                r += 1
            steps += 1
        
        return steps - 1
            


