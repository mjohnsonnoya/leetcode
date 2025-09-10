class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n
        ans = []
        path = []
        def dfs():
            if len(path) == n:
                ans.append(path[:])
            else:
                for i in range(len(used)):
                    if not used[i]:
                        path.append(nums[i])
                        used[i] = True
                        dfs()
                        used[i] = False
                        path.pop()
        dfs()
        return ans
            

        
