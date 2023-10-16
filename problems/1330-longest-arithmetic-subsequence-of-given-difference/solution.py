class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        cache = {}
        n = len(arr)
        
        if n <= 1:
            return n
        
        maxlength = 1
        
        for i in range(n):
            diff = arr[i] - difference
            cache[arr[i]] = cache.get(diff, 0) + 1
            maxlength = max(maxlength, cache[arr[i]])
            
        return maxlength
