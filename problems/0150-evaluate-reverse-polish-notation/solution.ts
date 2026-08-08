function evalRPN(tokens: string[]): number {
    const ops = new Set<string>(['+', '-', '*', '/']);

    const stack: number[] = [];

    for (const c of tokens) {
        if (ops.has(c)) {
            const b = stack.pop();
            const a = stack.pop();

            switch (c) {
                case '+':
                    stack.push(a + b);
                    break;
                case '-':
                    stack.push(a - b);
                    break;
                case '*':
                    stack.push(a * b);
                    break;
                case '/':
                    stack.push(Math.trunc(a / b));
                    break;
            }
        }

        else {
            stack.push(Number(c));
        }
        // console.log(stack);
    }

    return stack[0];
};
