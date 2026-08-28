function largestRectangleArea(heights: number[]): number {
    const n = heights.length;
    const stack: [number, number][] = [];
    let maxArea = 0;

    for (let i = 0; i < heights.length; i++) {
        const height = heights[i];
        let start = i;
        while (stack.length > 0 && stack[stack.length - 1][1] >= height) {
            const [idx, prevHeight] = stack.pop();
            const area = (i - idx) * prevHeight;
            maxArea = Math.max(maxArea, area);
            start = idx;
        }

        stack.push([start, height]);
    }

    while (stack.length > 0) {
        const [idx, prevHeight] = stack.pop();
        const area = (n - idx) * prevHeight;
        maxArea = Math.max(maxArea, area);
    }

    return maxArea;
};
