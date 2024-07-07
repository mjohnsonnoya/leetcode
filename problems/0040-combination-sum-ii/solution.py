class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        stack = []
        res = []
        def dfs(i, total):
            print("index: ",i, "total: ",total, "stack: ", stack)
            if total == target:
                res.append(stack.copy())
                return
            if i >= len(candidates) or total > target:
                return
            else:
                stack.append(candidates[i])
                dfs(i + 1, total + candidates[i])
                stack.pop()
                while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                    i += 1
                dfs(i + 1, total)
        dfs(0,0)
        return res
            

            
            

