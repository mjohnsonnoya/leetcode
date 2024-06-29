class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for i, c in enumerate(nums):
            if target - c in vals:
                return [vals[target - c], i]
            else:
                vals[c] = i
