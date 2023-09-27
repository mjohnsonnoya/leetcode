class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                val = nums[left] + nums[right] + nums[i]
                if val < 0:
                    left += 1
                elif val > 0:
                    right -= 1
                else:
                    res.append([nums[left],nums[right],nums[i]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res
        # while a < len(nums):
        #     val = nums[a]
        #     l = a + 1
        #     r = len(nums) - 1
        #     while l < r:
        #         if nums[l] + nums[r] + val == 0:
        #             res.append([nums[l],nums[r],val])
        #         elif nums[l] + nums[r] + val > 0: 
        #             r -=1
        #         else:
        #             l += 1
        #     a += 1
        # return res
        # solset = set()
        # res = []
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 if tuple(set([nums[i],nums[j],nums[k]])) not in solset:
        #                     res.append([nums[i],nums[j],nums[k]])
        #                     solset.add(tuple(set([nums[i],nums[j],nums[k]])))
        # return res
