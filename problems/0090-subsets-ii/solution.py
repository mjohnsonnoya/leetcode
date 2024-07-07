class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        stack = []
        res = []
        def recursive(i):
            if i == len(nums):
                res.append(stack.copy())
                return
            stack.append(nums[i])
            recursive(i + 1)
            stack.pop()
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            recursive(i + 1)
        recursive(0)
        return res


