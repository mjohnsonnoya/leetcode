class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        freq = {}
        ans = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        buckets = [[] for i in range(len(nums) + 1)]
        for key, val in freq.items():
            buckets[val].append(key)
        for i in range(len(buckets) - 1, 0, -1):
            if buckets[i]:
                for j in buckets[i]:
                    ans.append(j)
                    if len(ans) == k:
                        return ans



