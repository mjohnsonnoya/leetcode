function carFleet(target: number, position: number[], speed: number[]): number {
    const stack: [number, number][] = [];

    for (let i = 0; i < position.length; i++) {
        stack.push([position[i], speed[i]]);
    }

    stack.sort((a, b) => a[0] - b[0]);

    // console.log(stack);

    let numFleets = 0;

    while (stack.length > 0) {
        const [currPos, currSpeed] = stack.pop();

        const currArrivalTime = (target - currPos) / currSpeed;

        if (stack.length === 0) {
            numFleets += 1;
            break;
        }

        const [prevPos, prevSpeed] = stack[stack.length - 1];

        const prevArrivalTime = (target - prevPos) / prevSpeed;

        if (prevArrivalTime <= currArrivalTime) {
            stack.pop();
            stack.push([currPos, currSpeed]);
        }

        else {
            numFleets += 1;
        }
    }

    return numFleets;


};
