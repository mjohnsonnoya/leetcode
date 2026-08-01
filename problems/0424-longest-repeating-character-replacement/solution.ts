function characterReplacement(s: string, k: number): number {
    let l = 0;
    const count = new Array<number>(26).fill(0);
    const charCodeA = 'A'.charCodeAt(0);
    let maxFreq = 1;
    let maxLength = 1;

    for (let r = 0; r < s.length; r++) {
        const rightIndex = s.charCodeAt(r) - charCodeA;
        count[rightIndex] += 1;

        if (count[rightIndex] > maxFreq) {
            maxFreq = count[rightIndex];
        }

        while ((r - l + 1) - maxFreq > k) {
            count[s.charCodeAt(l) - charCodeA]--;
            l += 1;
        }

        if ((r - l + 1) - maxFreq <= k) {
            maxLength = Math.max(maxLength, (r - l + 1));
        }

    }

    return maxLength;
};
