class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        stack = []
        res = []
        def dfs(candidates, total):
            if total == target:
                res.append(stack.copy())
            if not candidates:
                return
            if candidates[0] + total > target:
                return
            i = 0
            stack.append(candidates[i])
            dfs(candidates[i+1:], total + candidates[i])
            stack.pop()
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(candidates[i+1:], total)
        dfs(candidates, 0)
        return res
