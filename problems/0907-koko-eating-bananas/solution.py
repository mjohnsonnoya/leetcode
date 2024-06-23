class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 1
        l, r = 1, max(piles)
        ans = max(piles) + 1
        while l <= r:
            k = l + (r - l)//2
            hours = 0
            for pile in piles:
                hours += -(pile // -k)
            if hours <= h:
                ans = min(ans, k)
                r = k - 1
            else:
                l = k + 1
        return ans
