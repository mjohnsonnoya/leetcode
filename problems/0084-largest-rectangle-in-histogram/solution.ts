function largestRectangleArea(heights: number[]): number {
    const stack: [number, number][] = [];
    let maxArea = 0;

    for (let i = 0; i < heights.length; i++) {
        const height = heights[i];
        let start = i;
        while (stack.length !== 0 && height <= stack[stack.length - 1][1]) {
            const [prevIdx, prevHeight] = stack.pop();
            const area = prevHeight * (i - prevIdx);
            maxArea = Math.max(area, maxArea);
            start = prevIdx;
        }

        stack.push([start, height]);
    }

    while (stack.length !== 0) {
        const [idx, height] = stack.pop();
        const area = height * (heights.length - idx);
        maxArea = Math.max(area, maxArea);
    }

    return maxArea;
};
