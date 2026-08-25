function checkInclusion(s1: string, s2: string): boolean {
    const needed = new Map<string, number>();

    for (const char of s1) {
        needed.set(char, (needed.get(char) ?? 0) + 1);
    }

    let numNeeded = s1.length;

    let l = 0;

    for (let r = 0; r < s2.length; r++) {
        const rightChar = s2[r];
        needed.set(rightChar, (needed.get(rightChar) ?? 0) - 1);

        numNeeded -= 1;

        while (needed.get(rightChar) < 0) {
            const leftChar = s2[l];
            needed.set(leftChar, (needed.get(leftChar) ?? 0) + 1);
            numNeeded += 1;
            l += 1;
        }

        if (numNeeded === 0) {
            return true;
        }
    }

    return false;
};
