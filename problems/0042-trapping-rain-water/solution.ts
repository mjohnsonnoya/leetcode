function trap(height: number[]): number {
    if (height.length <= 2) {return 0};

    let l = 0;
    let r = height.length - 1;

    let leftMax = height[l];
    let rightMax = height[r];

    let ans = 0;

    while (l <= r) {
        if (leftMax <= rightMax) {
            leftMax = Math.max(leftMax, height[l]);
            ans += leftMax - height[l];
            l += 1;
            continue;
        }

        else {
            rightMax = Math.max(rightMax, height[r]);
            ans += rightMax - height[r];
            r -= 1;
            continue;
        }
    }

    return ans;
};
