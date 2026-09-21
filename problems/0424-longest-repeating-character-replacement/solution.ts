function characterReplacement(s: string, k: number): number {
    let l = 0;

    const count = new Map<string, number>();

    let maxFreq = 0;

    let maxLen = 0;

    for (let r = 0; r < s.length; r++) {
        const rightChar = s[r];
        count.set(rightChar, (count.get(rightChar) ?? 0) + 1);

        maxFreq = Math.max(count.get(rightChar), maxFreq);

        while (r - l + 1 - maxFreq > k) {
            const leftChar = s[l];
            count.set(leftChar, count.get(leftChar) - 1);
            l += 1;
        }

        maxLen = Math.max((r - l + 1), maxLen);
    }

    return maxLen;
};
