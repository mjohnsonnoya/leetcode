class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        lmax = [0] * len(height)
        rmax = [0] * len(height)
        total_water = 0
        
        lmax[0] = height[0]
        for i in range(1, len(height)):
            lmax[i] = max(height[i],lmax[i - 1])
        
        rmax[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            rmax[i] = max(height[i],rmax[i + 1])
        
        for i, x in enumerate(height):
            water = min(lmax[i],rmax[i]) - x
            if water > 0:
                total_water += water
        return total_water
        
        
        

