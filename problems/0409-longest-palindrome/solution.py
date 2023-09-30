class Solution:
    def longestPalindrome(self, s: str) -> int:
        maxPalindrome = 0
        charDict = {}
        hasOdd = False
        for char in s:
                charDict[char] = charDict.get(char,0) + 1
                
        for value in charDict.values():
                
                if value % 2 == 0:
                        maxPalindrome += value
                else:
                        hasOdd = True
                        maxPalindrome += value - 1
        if hasOdd == True:
                maxPalindrome += 1
        return maxPalindrome        
        
