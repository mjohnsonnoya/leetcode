class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(l,r):
                while l <= r:
                        m = (l+r)//2
                        if nums[m] == target:
                                return m
                        elif nums[m] > target:
                                r = m-1
                        else:
                                l = m + 1
                return -1
        l,r = 0, len(nums) -1
        while l <= r:
                m = (l+r)//2
                if nums[m] == target:
                        return m
                # left side is sorted
                elif nums[l] <= nums[m]:
                        if nums[l] <= target <= nums[m]:
                                result = helper(l,m)
                                if result != -1:
                                        return result
                                else:
                                        break
                        l = m + 1
                # right side is sorted
                elif nums[m] <= nums[r]:
                        if nums[m] <= target <= nums[r]:
                                result = helper(m,r)
                                if result != -1:
                                        return result
                                else:
                                        break
                        r = m - 1
                        
                
        return -1
