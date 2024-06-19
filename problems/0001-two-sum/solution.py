class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for idx, num in enumerate(nums):
            residual = target - num
            if residual in vals:
                return [vals[residual], idx]
            else:
                vals[num] = idx
        
