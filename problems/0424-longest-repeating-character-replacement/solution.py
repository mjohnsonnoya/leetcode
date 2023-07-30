class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # def most_freq(substr):
        #     freqdict = defaultdict(int)
        #     maxfreq = 0
        #     for i in substr:
        #         freqdict[i] += 1
        #     for value in freqdict.values():
        #         if value > maxfreq:
        #             maxfreq = value
        #     return maxfreq
        count = defaultdict(int)
        max_freq = max_len = 0
        end = start = 0

        while end < len(s):
            count[s[end]] += 1
            max_freq = max(max_freq, count[s[end]])

            while (end - start + 1) - max_freq > k: 
                count[s[start]] -= 1
                start += 1

            max_len = max(max_len, end - start + 1)
            end += 1

        return max_len


        # for i in range(len(s)):
        #   for j in range(i+1,len(s)+1):
        #      mf, mc = most_freq(s[i:j])
        #      if ((len(s[i:j])) - mf) <= k:
        #          longest = max(longest, len(s[i:j]))    

                 
            
                


        
