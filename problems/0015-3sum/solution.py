class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                threesum = nums[j]+nums[k]+nums[i]
                if (threesum == 0):
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while nums[j] == nums[j-1] and j < k:
                        j+=1
                if (threesum > 0):
                    k -=1
                elif (threesum < 0):
                    j +=1
        return res
        








