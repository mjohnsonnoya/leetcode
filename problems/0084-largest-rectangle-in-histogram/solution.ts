function largestRectangleArea(heights: number[]): number {
    const stack: [number, number][] = [];

    let maxArea = 0;

    const n = heights.length;

    for (let i = 0; i < heights.length; i++) {
        const height = heights[i];
        let l = i;

        while (stack.length !== 0 && stack[stack.length - 1][1] >= height) {
            const [idx, prevHeight] = stack.pop();
            const area = prevHeight * (i - idx);

            maxArea = Math.max(maxArea, area);
            l = idx;
        }

        stack.push([l, height]);
    }

    while (stack.length !== 0) {
        const [idx, height] = stack.pop()

        const area = height * (n - idx);

        maxArea = Math.max(maxArea, area);
    }

    return maxArea;
};
