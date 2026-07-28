function checkInclusion(s1: string, s2: string): boolean {
    let l = 0;
    let r = 0;

    const count = Array<number>(26).fill(0);
    const aCharCode = 'a'.charCodeAt(0);

    for (let i = 0; i < s1.length; i++) {
        count[s1.charCodeAt(i) - aCharCode]--;
    }

    while (r < s2.length) {

        count[s2.charCodeAt(r) - aCharCode]++;

        let allZero = true;
        for (const c of count) {
            if (c !== 0) {
                allZero = false;
            }
        }

        if (allZero) {
            return allZero;
        }

        while (count[s2.charCodeAt(r) - aCharCode] > 0) {
            count[s2.charCodeAt(l) - aCharCode]--;
            l += 1;
        }

        r += 1;
    }

    return false;
};
