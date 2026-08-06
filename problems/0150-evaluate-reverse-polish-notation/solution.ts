function evalRPN(tokens: string[]): number {
    const stack: number[] = [];

    const ops = new Set<string>(['+', '-', '*', '/']);

    for (const token of tokens) {
        if (ops.has(token)) {
            const b = stack.pop();
            const a = stack.pop();

            if (token === '+') {
                stack.push(a + b);
            }

            else if (token === '-') {
                stack.push(a - b);
            }

            else if (token === '*') {
                stack.push(a * b);
            }

            else {

                stack.push(Math.trunc(a / b));
            }
        }

        else {
            stack.push(Number(token));
        }
    }

    return stack[0];
};
