class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:              # base case
            return [[]]
        ans = []
        for i in range(len(nums)):
            perms = [[nums[i]] + end for end in self.permute(nums[:i] + nums[i+1:])]
            ans.extend(perms)
        
        return ans
        
