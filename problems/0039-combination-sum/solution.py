class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        stack = []
        res = []
        def dfs(total, i):
            if total > target or i >= len(candidates):
                return
            if total == target:
                res.append(stack.copy())
            else:
                stack.append(candidates[i])
                dfs(total + candidates[i], i)
                stack.pop()
                dfs(total, i + 1)
        dfs(0, 0)
        return res


