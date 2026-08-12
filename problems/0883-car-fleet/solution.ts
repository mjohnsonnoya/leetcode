function carFleet(target: number, position: number[], speed: number[]): number {
    let stack: number[][] = [];
    for (let i = 0; i < position.length; i++) {
        stack.push([position[i], speed[i]]);
    }

    stack = stack.sort((a, b) => a[0] - b[0]);

    let fleets = 0;

    while (stack.length !== 0) {
        const ps = stack.pop();
        const distance = target - ps[0];
        const arrivalTime = distance / ps[1];

        if (stack.length === 0) {
            fleets += 1;
            break;
        }

        const psbehind = stack[stack.length - 1];
        if ((target - psbehind[0])/(psbehind[1]) <= arrivalTime) {
            stack.pop();
            stack.push(ps);
        }

        else {
            fleets += 1;
        }
    }

    return fleets;
};
