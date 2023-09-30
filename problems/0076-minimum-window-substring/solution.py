class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        charsNeeded = {}
        
        for char in t:
            charsNeeded[char] = charsNeeded.get(char, 0) + 1
        
        substringChars = {}
        
        requiredChars = len(charsNeeded)
        formedChars = 0
        
        minSubstringLength = float('inf')
        minSubstringStart = 0
        
        while r < len(s):
            if s[r] in charsNeeded:
                substringChars[s[r]] = substringChars.get(s[r], 0) + 1
                if substringChars[s[r]] == charsNeeded[s[r]]:
                    formedChars += 1
            
            while l <= r and formedChars == requiredChars:
                if r - l + 1 < minSubstringLength:
                    minSubstringLength = r - l + 1
                    minSubstringStart = l
                
                if s[l] in charsNeeded:
                    substringChars[s[l]] -= 1
                    if substringChars[s[l]] < charsNeeded[s[l]]:
                        formedChars -= 1
                
                l += 1
                
            r += 1
        
        return "" if minSubstringLength == float('inf') else s[minSubstringStart:minSubstringStart+minSubstringLength]

