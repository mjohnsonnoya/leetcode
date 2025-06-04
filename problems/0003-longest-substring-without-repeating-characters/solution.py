class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        q = deque()
        maxstring = ''
        size = 0
        for char in s:
            while char in visited:
                visited.remove(q.popleft())
            q.append(char)
            visited.add(char)
            if len(q) > size:
                size = len(q)
        return size

            
