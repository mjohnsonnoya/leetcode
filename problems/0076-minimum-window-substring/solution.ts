function minWindow(s: string, t: string): string {
    let leftMin = -1
    let minLength = Infinity;

    let numNeeded = t.length;

    const need = new Map<string, number>();
    for (const char of t) {
        need.set(char, (need.get(char) ?? 0) + 1);
    }

    let l = 0;

    for (let r = 0; r < s.length; r++) {
        const rightChar = s[r];
        need.set(rightChar, (need.get(rightChar) ?? 0) - 1);

        if (need.get(rightChar) >= 0) {
            numNeeded -= 1;
        }

        if (numNeeded === 0) {
            while (need.get(s[l]) < 0) {
                const leftChar = s[l];
                need.set(leftChar, need.get(leftChar) + 1);
                l += 1;
            }
            if ((r - l + 1) < minLength) {
                minLength = (r - l + 1);
                leftMin = l;
            }
            const leftChar = s[l];
            numNeeded += 1;
            need.set(leftChar, need.get(leftChar) + 1);
            l += 1;
        }
    }

    return (leftMin === -1) ? "" : s.slice(leftMin, leftMin + minLength);
};
