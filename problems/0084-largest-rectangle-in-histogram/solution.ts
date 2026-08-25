function largestRectangleArea(heights: number[]): number {
    const n = heights.length;
    const stack: [number, number][] = [];

    let maxArea = 0;

    for (let i = 0; i < n; i++) {
        const height = heights[i];
        let start = i;
        while (stack.length > 0 && stack[stack.length - 1][0] >= height) {
            const [prevHeight, idx] = stack.pop();

            const area = prevHeight * (i - idx);
            maxArea = Math.max(area, maxArea);
            start = idx;
        }

        stack.push([height, start]);
    }

    while (stack.length > 0) {
        const [height, idx] = stack.pop();
        const area = height * (n - idx);

        maxArea = Math.max(area, maxArea);
    }

    return maxArea;
};
