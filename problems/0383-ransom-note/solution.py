class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_count = defaultdict(int)
        for c in magazine:
            mag_count[c] += 1
        for c in ransomNote:
            mag_count[c] -= 1
            if mag_count[c] < 0:
                return False
    
        return True
