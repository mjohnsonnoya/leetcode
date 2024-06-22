class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        def binarySearch(l, r, target):
            while l <= r:
                m = l + (r - l)//2
                if nums[m] == target:
                    return m
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1
        while l <= r:
            m = l + (r - l)//2
            if nums[m] == target:
                return m
            elif nums[m] < target <= nums[r]:
                l = m + 1
                return binarySearch(l, r, target)
            elif nums[l] <= target < nums[m]:
                r = m - 1
                return binarySearch(l, r, target)
            elif nums[m] > nums[r]:
                l = m + 1
            elif nums[l] > nums[m]:
                r = m - 1
            else:
                return -1
        return -1
