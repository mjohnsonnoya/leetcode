function isValid(s: string): boolean {
    const stack: string[] = [];

    const mapping = new Map<string, string>([[']', '['], [')', '('], ['}', '{']]);

    for (const char of s) {
        if (stack.length === 0) {
            stack.push(char);
        }

        else if (mapping.has(char) && stack[stack.length - 1] === mapping.get(char)) {
            stack.pop();
        }

        else {
            stack.push(char);
        }


    }

    return stack.length === 0;
};
