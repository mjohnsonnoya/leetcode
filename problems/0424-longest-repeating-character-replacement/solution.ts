function characterReplacement(s: string, k: number): number {
    let l = 0;
    let r = 0;

    let maxFreq = 1;
    let ans = 1;

    const count = new Array<number>(26).fill(0);
    const charCodeA = 'A'.charCodeAt(0);

    while (r < s.length) {
        count[s.charCodeAt(r) - charCodeA]++;
        if (count[s.charCodeAt(r) - charCodeA] >= maxFreq) {
            maxFreq = count[s.charCodeAt(r) - charCodeA];
        }

        if ((r - l + 1) - maxFreq <= k) {
            ans = Math.max(ans, (r - l + 1));
        }

        while ((r - l + 1) - maxFreq > k) {
            count[s.charCodeAt(l) - charCodeA]--;
            l += 1;
        }
        
        r += 1;
    }

    return ans;
};
