function checkInclusion(s1: string, s2: string): boolean {

    const needed = new Array<number>(26).fill(0);
    const aCharCode = 'a'.charCodeAt(0);

    for (let i = 0; i < s1.length; i++) {
        needed[s1.charCodeAt(i) - aCharCode]++;
    }

    let l = 0;

    for (let r = 0; r < s2.length; r++) {
        needed[s2.charCodeAt(r) - aCharCode]--;
        if (needed[s2.charCodeAt(r) - aCharCode] === 0) {
            let satisfied = true;
            for (const x of needed) {
                if (x !== 0) {
                    satisfied = false;
                }
            }

            if (satisfied) {
                return true;
            }
        }

        while (needed[s2.charCodeAt(r) - aCharCode] < 0) {
            needed[s2.charCodeAt(l) - aCharCode]++;
            l += 1
        }
    }

    return false;
};
