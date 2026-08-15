function characterReplacement(s: string, k: number): number {
    let maxLength = 1;

    const n = s.length;

    let l = 0;

    const count = new Map<string, number>();
    let maxFreq = 1;

    for (let r = 0; r < n; r++) {
        const rightChar = s[r];
        count.set(rightChar, (count.get(rightChar) ?? 0) + 1);

        if (count.get(rightChar) > maxFreq) {
            maxFreq = count.get(rightChar);
        }


        if (r - l + 1 - maxFreq <= k) {
            maxLength = Math.max(maxLength, r - l + 1);
        }

        while (r - l + 1 - maxFreq > k) {
            const leftChar = s[l];
            count.set(leftChar, count.get(leftChar) - 1);
            l += 1;
        }
    }

    return maxLength;
};
