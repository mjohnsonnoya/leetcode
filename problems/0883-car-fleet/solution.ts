function carFleet(target: number, position: number[], speed: number[]): number {
    let fleets = 0;
    let stack: number[][] = [];

    for (let i = 0; i < position.length; i++) {
        stack.push([position[i], speed[i]]);
    }

    stack.sort((a , b) => (a[0] - b[0]));

    while (stack.length > 0) {
        const [pos, v] = stack.pop();
        const arrivalTime = (target - pos) / v;

        if (stack.length === 0 ) {
            fleets += 1;
        }

        else {
            const [prevPos, prevV] = stack[stack.length - 1];

            const nextArrivalTime = (target - prevPos) /prevV;

            if (nextArrivalTime <= arrivalTime) {
                stack.pop()
                stack.push([pos, v]);
            }

            else {
                fleets += 1;
            }
        }



    }

    return fleets;
};
