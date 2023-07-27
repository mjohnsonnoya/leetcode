class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set(nums)

        for i in nums:
            j = i
            l = 1
            if (i-1) not in numset:
                while (j + 1) in numset:
                    j += 1
                    l += 1
                longest = max(l,longest)
        return longest

