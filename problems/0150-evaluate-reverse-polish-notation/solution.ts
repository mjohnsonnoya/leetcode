function evalRPN(tokens: string[]): number {
    const stack: number[] = [];

    const ops: Set<string> = new Set<string>(['+', '-', '*', '/']);

    for (const token of tokens) {
        if (ops.has(token)) {
            const b: number = stack.pop();
            const a: number = stack.pop();
            switch (token) {
                case "+":
                    stack.push(a + b);
                    break;
                case "-":
                    stack.push(a - b);
                    break;
                case "*":
                    stack.push(a * b);
                    break;
                case "/":
                    stack.push(Math.trunc(a / b));
                    break;
            }


        }

        else {stack.push(Number(token));}
    }


    return stack[stack.length - 1];
};
