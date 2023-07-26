class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results =[0]*len(nums)
        prefix = [0]*len(nums)
        postfix =[0]*len(nums)
        prefix[0] = nums[0]
        postfix[-1] = nums[-1]
        for i in range(len(nums) - 1):
            prefix[i+1] = nums[i + 1] * prefix[i]
            postfix[-(i+2)] = nums[-(i+2)] * postfix[-(i+1)]
        for i in range(len(results)):
            if i == 0:
                results[i] = postfix[i+1]
            elif (i == len(results)-1):
                results[i] = prefix[i-1]
            else:
                results[i] = prefix[i-1]*postfix[i+1] 
        return results
