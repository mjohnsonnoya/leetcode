function trap(height: number[]): number {
    let l = 0;
    let r = height.length - 1;

    let leftMax = height[l];
    let rightMax = height[r];

    let water = 0;

    while (l <= r) {
        if (leftMax <= rightMax) {
            leftMax = Math.max(leftMax, height[l]);
            water += leftMax - height[l];
            l += 1;
        }

        else {
            rightMax = Math.max(rightMax, height[r]);
            water += rightMax - height[r];
            r -= 1;
        }
    }
    
    return water;""
};
