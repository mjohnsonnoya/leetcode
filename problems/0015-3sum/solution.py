class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        triplets = []
        nums.sort()
        while i < len(nums) - 2:
            res = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[l] + nums[r]
                if total > res:
                    r -=1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif total < res:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                else:
                    triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -=1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
            
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i-1]:
                i += 1
        return triplets
