class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            idx = (l + r)//2
            if nums[idx] == target:
                return idx
            elif nums[idx] < target:
                l = idx + 1
            elif nums[idx] > target:
                r = idx - 1
        return -1
            
            
