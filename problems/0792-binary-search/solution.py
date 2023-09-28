class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) -1
        while l <= r:
            k = l+ ((r-l)//2)
            if nums[k] == target:
                return k
            if nums[k] > target:
                r = k - 1
            if nums[k] < target:
                l = k + 1
        return -1
