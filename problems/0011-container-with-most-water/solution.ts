function maxArea(height: number[]): number {
    let l = 0;
    let r = height.length - 1;
    let maxArea = 0;

    while (l < r) {
        const leftHeight = height[l];
        const rightHeight = height[r];
        const area = (r - l) * Math.min(leftHeight, rightHeight);
        maxArea = Math.max(maxArea, area);

        if (leftHeight <= rightHeight) {
            l += 1;
        }

        else {
            r -= 1;
        }

    }

    return maxArea;
};
