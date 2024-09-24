class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, ans, total):
            if total > target or i >= len(candidates):
                return
            if total == target:
                res.append(ans.copy())
                return
            ans.append(candidates[i])
            dfs(i, ans, total + candidates[i])
            ans.pop()
            dfs(i + 1, ans, total)
        
        dfs(0, [], 0)
        return res
            
