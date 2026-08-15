function isValid(s: string): boolean {
    const equiv = new Map<string, string>([['(', ')'], ['[', ']'], ['{', '}']]);
    const stack: string[] = [];

    for (const char of s) {
        if (stack.length === 0) {
            stack.push(char);
            continue;
        }

        const top = stack[stack.length - 1];
        if (equiv.has(top) && equiv.get(top) === char) {
            stack.pop();
            continue;
        }

        stack.push(char);
    }

    return stack.length === 0;
};
