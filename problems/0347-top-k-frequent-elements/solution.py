class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        counts = [[] for _ in range(len(nums) + 1)]

        for llave in freq:
            counts[freq[llave]].append(llave)
        
        for i in range(len(counts) - 1, 0, -1):
            if counts[i]:
                for num in counts[i]:
                    ans.append(num)
                    if len(ans) == k:
                        return ans
        
        return ans
                
