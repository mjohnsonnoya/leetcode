class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        super_slow = 0
        while True:
            slow = nums[slow]
            super_slow = nums[super_slow]
            if slow == super_slow:
                 return slow
