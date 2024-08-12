class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        n = len(nums)
        rob1, rob2 = nums[1], max(nums[1], nums[2])
        for i in range(3, n):
            curr_rob = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = curr_rob
        
        c1 = rob2

        rob1, rob2 = nums[0], max(nums[0], nums[1])
        for i in range(2, n - 1):
            curr_rob = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = curr_rob
        c2 = rob2
        return max(c1, c2)




