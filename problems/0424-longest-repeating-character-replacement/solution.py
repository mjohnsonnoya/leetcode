class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        counts = {}
        max_count = 0
        while r < len(s):
            counts[s[r]] = counts.get(s[r], 0) + 1
            max_count = max(max_count, counts[s[r]])
            if r - l + 1 - max_count > k:
                counts[s[l]] -= 1
                l += 1
            r += 1
        return r - l



