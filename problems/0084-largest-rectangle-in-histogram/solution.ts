function largestRectangleArea(heights: number[]): number {
    const stack: [number, number][] = []
    let maxArea = 0;
    const n = heights.length;
    for (let r = 0; r < n; r++) {
        const height = heights[r];

        let idx = r;

        while (stack.length > 0 && height < stack[stack.length - 1][1]) {
            const [prevIdx, prevHeight] = stack.pop();
            let area = (r - prevIdx) * prevHeight

            idx = prevIdx;

            maxArea = Math.max(maxArea, area);
        }

        stack.push([idx, height]);
    }

    while (stack.length > 0) {
            const [prevIdx, prevHeight] = stack.pop();
            let area = (n - prevIdx) * prevHeight

            maxArea = Math.max(maxArea, area);
    }

    

    return maxArea;
};
