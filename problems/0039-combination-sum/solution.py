import queue
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(total,i,curr):
                if total == target:
                        res.append(curr)
                elif total < target:
                        dfs(total+candidates[i],i,curr + [candidates[i]])
                        if i < len(candidates) - 1:
                                i+=1
                                dfs(total,i,curr)
                else:
                        return
        dfs(0,0,[])
        return res
