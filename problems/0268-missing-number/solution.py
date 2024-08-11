class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        val = 0
        n = len(nums)
        for num in range(1, n + 1):
            val ^= num
        
        for num in nums:
            val ^= num
        return val
