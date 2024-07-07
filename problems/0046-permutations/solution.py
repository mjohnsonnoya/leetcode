class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack = []
        res = []
        def permute(vals):
            if not vals:
                res.append(stack.copy())
                return
            for i in range(len(vals)):
                stack.append(vals[i])
                permute(vals[:i] + vals[i + 1:])
                stack.pop()

        permute(nums)
        return res

