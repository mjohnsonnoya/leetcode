class Solution:
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)
        subset_total = total // k
        if not k * subset_total == total:
            return False
        
        n = len(nums)
        dp = [-1] * (1 << n)
        
        def helper(k, mask, current_sum):
            if k == 0:
                return mask == (1 << n) - 1
            
            if dp[mask] != -1:
                return dp[mask]
            
            ans = False
            
            for i in range(n):
                if mask & (1 << i) or current_sum + nums[i] > subset_total:
                    continue
                
                new_mask = mask | (1 << i)
                new_sum = current_sum + nums[i]
                
                # If the new subset total is reached, decrement k and reset current_sum
                if new_sum == subset_total:
                    ans = helper(k-1, new_mask, 0)
                else:
                    ans = helper(k, new_mask, new_sum)
                
                # If a solution is found, break the loop
                if ans:
                    break
            
            dp[mask] = ans
            return ans
        
        return helper(k, 0, 0)

# Test case: [4,3,2,3,5,2,1], k=4


