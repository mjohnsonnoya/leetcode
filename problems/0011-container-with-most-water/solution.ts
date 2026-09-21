function maxArea(height: number[]): number {
    let l = 0;
    let r = height.length - 1;

    let maxWater = 0;

    while (l < r) {
        const water = (r - l) * Math.min(height[l], height[r]);

        maxWater = Math.max(water, maxWater);

        if (height[l] <= height[r]) {
            l += 1;
        }

        else {
            r -= 1;
        }
    }

    return maxWater;


};
