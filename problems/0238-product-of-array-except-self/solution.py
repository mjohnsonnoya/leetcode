class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prev = 1
        post = 1
        res = [1] * n

        for i in range(len(nums) - 1):
            prev *= nums[i]
            post *= nums[n - 1 - i]
            res[i + 1] = res[i + 1] * prev
            res[n -  1 - i - 1] = res[n - 1 - i - 1] * post

        return res       
        # prev = [1] * len(nums)
        # post = [1] * len(nums)  
        # for i in range(len(nums)):
        #     if i == 0:
        #         prev[i] = nums[i]
        #         post[n - 1 - i] = nums[n - 1 - i]
        #     else:
        #         prev[i] = nums[i] * prev[i - 1]
        #         post[n - 1 - i] = nums[n - 1 - i] * post[n - i]

        # res = [1] * len(nums)
        # print(prev)
        # print(post)

        # for i in range(len(nums)):
        #     if i == 0:
        #         res[i] = post[i + 1]
        #     elif i == len(nums) - 1:
        #         res[i] = prev[i - 1]
        #     else:
        #         res[i] = prev[i - 1] * post[i + 1]
        
        # return res
