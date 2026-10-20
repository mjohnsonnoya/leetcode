function characterReplacement(s: string, k: number): number {

    const count = new Map<string, number>();

    let maxCount = 0;
    let maxLen = 1;
    let l = 0;
    for (let r = 0; r < s.length; r++) {
        const rightChar = s[r];
        count.set(rightChar, (count.get(rightChar) ?? 0) + 1);

        maxCount = Math.max(maxCount, count.get(rightChar));

        while (r - l + 1 - maxCount > k) {
            const leftChar = s[l];
            count.set(leftChar, (count.get(leftChar) ?? 0) - 1);
            l += 1;
        }

        maxLen = Math.max((r - l + 1), maxLen);
    }

    return maxLen;
};
