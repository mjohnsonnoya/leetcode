class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        MAX = nums[0]
        MIN = nums[0]
        ans = max(MAX, MIN)

        for i in range(1, len(nums)):
            print(MAX)
            firstoption = MAX * nums[i]
            secondoption = MIN * nums[i]
            thirdoption = nums[i]
            
            MAX = max(firstoption, secondoption, thirdoption)
            MIN = min(firstoption, secondoption, thirdoption)
            ans = max(ans, MAX)

        return ans


