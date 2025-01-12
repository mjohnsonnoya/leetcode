class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        
        for key, val in count.items():
            freq[val].append(key)
        
        ans = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                ans.append(num)
                k -= 1
            if k <= 0:
                return ans
            



        
