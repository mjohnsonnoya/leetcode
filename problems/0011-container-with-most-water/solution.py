class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        l,r = 0, len(height) - 1
        area = lambda l,r : (r-l)*(min(height[l],height[r]))
        while l < r:
                result = max(result,area(l,r))
                if height[l] < height[r]:
                        l+=1
                else:
                        r-=1
        return result
