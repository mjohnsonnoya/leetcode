function checkInclusion(s1: string, s2: string): boolean {
    let numNeeded = s1.length;

    const count = new Map<string, number>();

    for (const char of s1) {
        count.set(char, (count.get(char) ?? 0) + 1);
    }

    let l = 0;

    for (let r = 0; r < s2.length; r++) {
        const rightChar = s2[r];
        count.set(rightChar, (count.get(rightChar) ?? 0) - 1);
        numNeeded -=1 ;

        while (count.get(rightChar) < 0) {
            const leftChar = s2[l];
            count.set(leftChar, count.get(leftChar) + 1);
            l += 1;
            numNeeded += 1;
        }

        if (numNeeded === 0) return true;

    }

    return false;


};
