class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        if n == 1:
            return [nums]
        
        for i in range(len(nums)):
            perms = [[nums[i]] + end for end in self.permute(nums[0:i] + nums[i + 1:])]
            ans.extend(perms)

        return ans

            
        


        

        
