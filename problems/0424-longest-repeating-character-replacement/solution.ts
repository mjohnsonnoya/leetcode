function characterReplacement(s: string, k: number): number {
    let maxFreq = 1;
    let maxLength = 1;

    const charCodeA = 'A'.charCodeAt(0);
    const count = new Array<number>(26).fill(0);

    let l = 0;
    let r = s.length - 1;

    for (r = 0; r < s.length; r++) {
        // console.log("r: ", r);
        // console.log("l: ", l);
        count[s.charCodeAt(r) - charCodeA] += 1;
        // console.log(count);
        if (count[s.charCodeAt(r) - charCodeA] > maxFreq) {
            maxFreq = count[s.charCodeAt(r) - charCodeA];
        }

        if ((r - l + 1) - maxFreq <= k) {
            maxLength = Math.max(maxLength, (r - l + 1));
        }

        while ((r - l + 1) - maxFreq > k) {
            count[s.charCodeAt(l) - charCodeA] -= 1;
            l += 1;
        }
    }

    return maxLength;
};
