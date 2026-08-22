function largestRectangleArea(heights: number[]): number {
    const stack: [number, number][] = [];
    const n = heights.length;
    let maxArea = 0;

    for (let i = 0; i < heights.length; i++) {
        let start = i;
        while (stack.length > 0 && stack[stack.length - 1][1] >= heights[i]) {
            const [idx, height] = stack.pop();
            const area = (i - idx) * height;
            maxArea = Math.max(area, maxArea);
            start = idx;
        }

        stack.push([start, heights[i]]);
    }

    while (stack.length > 0) {
        const [idx, height] = stack.pop();
        const area = (n - idx) * height;
        maxArea = Math.max(area, maxArea);
    }

    return maxArea;
};
