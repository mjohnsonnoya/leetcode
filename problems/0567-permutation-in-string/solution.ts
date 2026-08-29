function checkInclusion(s1: string, s2: string): boolean {
    const need = new Map<string, number>();

    for (const char of s1) {
        need.set(char, (need.get(char) ?? 0) + 1);
    }

    let numNeeded = s1.length;

    let l = 0;

    for (let r = 0; r < s2.length; r++) {
        const rightChar = s2[r];
        if (!need.has(rightChar)) {
            while (l < r) {
                const leftChar = s2[l];
                need.set(leftChar, need.get(leftChar) + 1);
                numNeeded += 1;
                l += 1;
            }
            l += 1;
        }

        else if (need.get(rightChar) === 0) {
            while (l < r && need.get(rightChar) === 0) {
                const leftChar = s2[l];
                need.set(leftChar, need.get(leftChar) + 1);
                numNeeded += 1;
                l += 1;
            }
            need.set(rightChar, need.get(rightChar) - 1);
            numNeeded -= 1;
        }

        else {
            need.set(rightChar, need.get(rightChar) - 1);
            numNeeded -= 1;
        }

        if (numNeeded === 0) {
            return true;
        }
    }

    return false;

};
