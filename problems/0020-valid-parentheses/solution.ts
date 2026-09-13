function isValid(s: string): boolean {
    const stack: string[] = [];

    const mapping = new Map([["(", ")"], ["[", "]"], ["{", "}"],]);

    for (const char of s) {
        if (stack.length === 0) {
            stack.push(char);
        }

        else {
            if (char === mapping.get(stack[stack.length - 1])) {
                stack.pop();
            }

            else {
                stack.push(char);
            }
        }
    }

    return (stack.length === 0);
};
