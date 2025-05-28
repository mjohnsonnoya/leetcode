class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1
        

        length = 0
        isodd = 0
        
        for k, val in counter.items():
            if val % 2 != 0:
                isodd = 1
            length += 2 * (val // 2)
        
        return length + isodd
