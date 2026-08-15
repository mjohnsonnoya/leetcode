function largestRectangleArea(heights: number[]): number {
    let maxArea = 0;
    const stack: number[][] = [];

    for (let i = 0; i < heights.length; i++) {
        const currHeight = heights[i];
        if (stack.length === 0) {
            stack.push([i, currHeight]);
        }

        else {
            let topStack = stack[stack.length - 1];
            if (topStack[1] <= currHeight) {
                stack.push([i, currHeight]);
            }

            else {
                while (stack.length > 0 && stack[stack.length - 1][1] > currHeight) {
                    topStack = stack.pop();
                    const area = (i - topStack[0]) * topStack[1];
                    maxArea = Math.max(maxArea, area);
                }
                stack.push([topStack[0], currHeight]);
            }
        }
    }

    while (stack.length > 0) {
        const topStack = stack.pop();

        const area = (heights.length - topStack[0]) * topStack[1];
        maxArea = Math.max(maxArea, area);
    }


    return maxArea;
};
