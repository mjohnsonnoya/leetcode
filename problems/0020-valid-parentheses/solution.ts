function isValid(s: string): boolean {
    const stack: string[] = [];
    const mapping = new Map<string, string>([['(', ')'], ['[', ']'], ['{', '}']]);

    for (const char of s) {
        if (stack.length !== 0 && mapping.has(stack[stack.length - 1]) && mapping.get(stack[stack.length - 1]) === char) {
                stack.pop();
        }

        else {
            stack.push(char);
        }
    }

    return stack.length === 0;
};
