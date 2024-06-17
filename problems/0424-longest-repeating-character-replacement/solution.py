class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 1
        word = {s[l]: 1}
        max_count = 1
        count = 1
        max_letter = 1
        while r < len(s):
            word[s[r]] = word.get(s[r],0) + 1
            count += 1
            if word[s[r]] >= max_letter:
                max_letter = word[s[r]]
            while count - max_letter > k:
                word[s[l]] = word[s[l]] - 1
                l += 1
                count -= 1
            max_count = max(count, max_count)
            r += 1

        return max_count
