class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(i, candidate):
            if i >= len(nums):
                ans.append(candidate.copy())
                return
            helper(i + 1, candidate)
            candidate.append(nums[i])
            helper(i + 1, candidate)
            candidate.pop()
        
        helper(0, [])
        return ans


