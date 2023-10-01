class Solution:
        def lengthOfLIS(self, nums: List[int]) -> int:
                tails = []
                for num in nums:
                        idx = self.BinSearch(tails,num)
                        if idx == len(tails):
                                tails.append(num)
                        else:
                                tails[idx] = num
                return len(tails)
        def BinSearch(self, nums,x):
                if not nums:
                        return 0
                l,r = 0, len(nums) - 1
                while l < r:
                        m = l + (r - l) // 2
                        if x <= nums[m]:
                                r = m
                        else:
                                l = m + 1
                if nums[l] < x:
                        return l + 1
                return l    
#         dp = [0 for _ in range(len(nums))]
#         for i in range(len(nums))[::-1]:
#                 candidates = []
#                 for j in range(i+1,len(nums)):
#                         if nums[j] > nums[i]:
#                                 candidates.append(j)
#                 if not candidates:
#                         dp[i] = 1
#                 else:
#                         dp[i] = 1+ max(dp[ix] for ix in candidates)
                        
#         return max(dp)
