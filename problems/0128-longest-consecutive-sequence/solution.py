class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        groups = {}

        for num in nums:
            groups[num] = num
            longest = 1
        
        for num in nums:
            i = 1
            while num in groups and num - i in groups:
                groups[num] = groups[num - i]
                del groups[num - i]
                longest = max(longest, num - groups[num] + 1)
                i += 1
        return longest
