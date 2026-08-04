function isValid(s: string): boolean {
    const stack: string[] = [];
    const mapping = new Map<string, string>([['(', ')'], ['{', '}'], ['[', ']']]);

    for (const c of s) {
        if (stack.length === 0) {
            stack.push(c);
        }

        else if (mapping.has(stack[stack.length - 1]) && (mapping.get(stack[stack.length - 1]) === c)) {
            stack.pop()
        }

        else {
            stack.push(c);
        }
    }

    return (stack.length === 0);
};
