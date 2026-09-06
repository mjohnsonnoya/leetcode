function checkInclusion(s1: string, s2: string): boolean {
    let numNeeded = s1.length;

    const needed = new Array(26).fill(0);

    const aCharCode = 'a'.charCodeAt(0);

    for (let i = 0; i < numNeeded; i++) {
        const index = s1.charCodeAt(i) - aCharCode;
        needed[index] += 1;
    }

    let l = 0;

    for (let r = 0; r < s2.length; r++) {
        const rightCharIndex = s2.charCodeAt(r) - aCharCode;
        needed[rightCharIndex] -= 1;
        numNeeded -= 1;

        while (needed[rightCharIndex] < 0) {
            let leftIndex = s2.charCodeAt(l) - aCharCode;
            numNeeded += 1;
            needed[leftIndex] += 1;
            l += 1;
        }

        if (numNeeded === 0) {
            return true;
        }
    }

    return false;


};
