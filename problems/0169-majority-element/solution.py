class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        curr = nums[0]
        val = 1
        for i in range(1, len(nums)):
            if val > 0:
                if nums[i] == curr:
                    val += 1
                else:
                    val -= 1
            else:
                curr = nums[i]
                val = 1
        
        return curr
        

