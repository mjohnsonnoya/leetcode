class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_freq = {}
        for char in magazine:
            char_freq[char] = char_freq.get(char, 0) + 1
          
        for char in ransomNote:
          char_freq[char] = char_freq.get(char, 0) - 1
          if char_freq[char] < 0:
            return False
        return True
