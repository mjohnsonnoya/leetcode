class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        # def recursive(l, r):
        #     m = l + (r - l)//2
        #     if nums[m] == target:
        #         return m
        #     elif m == l:
        #         return -1
        #     if nums[m] > target:
        #         return recursive(l, m)
        #     else:
        #         return recursive(m,r)

        # return recursive(l,r)
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
            
