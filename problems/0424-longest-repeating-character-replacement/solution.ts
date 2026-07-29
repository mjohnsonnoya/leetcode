function characterReplacement(s: string, k: number): number {
    let l = 0;

    const count = new Array<number>(26).fill(0);
    const charCodeA = 'A'.charCodeAt(0);
    let maxFreq = 1;
    let ans = 1;

    for (let r = 0; r < s.length; r++) {
        const rightIndex = s.charCodeAt(r) - charCodeA;
        const leftIndex = s.charCodeAt(l) - charCodeA;
        count[rightIndex]++;

        if (count[rightIndex] >= maxFreq) {
            maxFreq = count[rightIndex];
        }

        if ((r - l + 1) - maxFreq <= k) {
            ans = Math.max(ans, (r - l + 1));
        }

        if ((r - l + 1) - maxFreq > k) {
            count[leftIndex]--;
            l += 1;
        }
    }

    return ans;
};
