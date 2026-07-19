function maxArea(height: number[]): number {
    let l = 0
    let r = height.length - 1;

    let water = 0;

    while (l < r) {
        const area = (r - l) * Math.min(height[l], height[r]);
        water = Math.max(water, area);

        if (height[l] <= height[r]) {
            l += 1;
        }

        else {
            r -= 1;
        }
    }

    return water;
};
