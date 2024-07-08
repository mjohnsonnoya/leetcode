class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        stack = []
        res = []
        def dfs(i, total):
            if i >= len(candidates):
                return
            if total == target:
                res.append(stack.copy())
                return
            if total + candidates[i] > target:
                return
            stack.append(candidates[i])
            dfs(i, total + candidates[i])
            stack.pop()
            dfs(i + 1, total)
        dfs(0, 0)
        return res
            
            

