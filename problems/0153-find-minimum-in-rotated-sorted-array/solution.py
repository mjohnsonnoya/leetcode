class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            print("l: ", l)
            print("r: ", r)
            if nums[l - 1] >= nums[l]:
                return nums[l]
            if nums[(r + 1) % len(nums)] <= nums[r]:
                return nums[(r + 1) % len(nums)]
            m = l + (r - l)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        return nums[l]
