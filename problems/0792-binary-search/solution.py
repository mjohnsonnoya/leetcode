class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while True:
            m = l + (r - l)//2
            if nums[m] == target:
                return m
            elif m == l:
                return -1
            if nums[m] > target:
                r = m
            else:
                l = m
        return -1

        # def recursive(l, r):
        #     m = (r-l)//2 + l
        #     if nums[m] == target:
        #         return m
        #     elif l == r:
        #         return -1
        #     if nums[m] > target:
        #         r = m - 1
        #     else:
        #         l = m + 1
        #     return recursive(l, r)
        # return recursive(l, r)
