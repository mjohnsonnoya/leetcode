# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        if isBadVersion(l):
            return l
        while l <= r:
            m = l + (r - l)//2
            if isBadVersion(m) and not isBadVersion(m - 1):
                return m
            if not isBadVersion(m):
                l = m + 1
            else:
                r = m - 1
