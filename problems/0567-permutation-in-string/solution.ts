function checkInclusion(s1: string, s2: string): boolean {
    if (s2.length < s1.length) {
        return false;
    }

    const need = new Array<number>(26).fill(0);
    const aCharCode = 'a'.charCodeAt(0);

    let l = 0;

    for (let i = 0; i < s1.length; i++) {
        need[s1.charCodeAt(i) - aCharCode] += 1;
    }

    for (let r = 0; r < s2.length; r++) {
        need[s2.charCodeAt(r) - aCharCode] -= 1;

        if (need[s2.charCodeAt(r) - aCharCode] === 0) {
            let valid = true;
            for (const c of need) {
                if (c !== 0) {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                return valid;
            }
        }

        else if (need[s2.charCodeAt(r) - aCharCode] < 0)  {
            while (need[s2.charCodeAt(r) - aCharCode] < 0) {
                need[s2.charCodeAt(l) - aCharCode]++;
                l += 1;
            }
        }
    }

    return false;
};
