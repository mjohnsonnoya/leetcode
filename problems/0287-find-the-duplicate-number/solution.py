class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        superslow = 0
        while True:
            slow = nums[slow]
            superslow= nums[superslow]
            if slow == superslow:
                break
        return superslow

