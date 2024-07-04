class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        ans = []
        while i < len(nums) - 2:
            target = -nums[i]
            print(target)
            j = i + 1
            k = len(nums) - 1
            while j < k:
                val = nums[j] + nums[k]
                if val == target:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j + 1] == nums[j]:
                        j += 1
                    j += 1
                    while j < k and nums[k - 1] == nums[k]:
                        k -= 1
                    k -= 1
                elif val > target:
                    k -= 1
                else:
                    j += 1
            while i < len(nums) - 3 and nums[i + 1] == nums[i]:
                i += 1
            i += 1
        return ans
