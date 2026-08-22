function checkInclusion(s1: string, s2: string): boolean {
    const n = s2.length;
    const needed = new Array<number>(26).fill(0);
    const aCharCode = 'a'.charCodeAt(0);
    let numNeeded = s1.length;
    for (const char of s1) {
        const index = char.charCodeAt(0) - aCharCode;
        needed[index] += 1;
    }

    let l = 0;

    for (let r = 0; r < n; r++) {
        const rightIndex = s2.charCodeAt(r) - aCharCode;
        needed[rightIndex] -= 1;

        numNeeded -= 1;

        while (l <= r && needed[rightIndex] < 0) {
            const leftIndex = s2.charCodeAt(l) - aCharCode;
            needed[leftIndex] += 1;

            numNeeded += 1;

            l += 1;
        }

        if (numNeeded === 0) {
            return true;
        }
    }

    return false;
};
