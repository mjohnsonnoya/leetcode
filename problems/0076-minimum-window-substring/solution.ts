function minWindow(s: string, t: string): string {
    const counter = new Map<string, number>();

    for (const char of t) {
        counter.set(char, (counter.get(char) ?? 0) + 1);
    }

    let numNeeded = t.length;

    let l = 0;

    let minLength = Infinity;
    let minLeft = -1;

    for (let r = 0; r < s.length; r++) {
        const rightChar = s[r];
        counter.set(rightChar, (counter.get(rightChar) ?? 0) - 1);
        if (counter.get(rightChar) >= 0) {
            numNeeded -= 1;
        }

        while (counter.get(s[l]) < 0) {
            counter.set(s[l], (counter.get(s[l]) ?? 0) + 1);
            l += 1;
        }

        if (numNeeded === 0) {
            if ((r - l + 1) < minLength) {
                minLeft = l;
                minLength = r - l + 1;
            }
            counter.set(s[l], (counter.get(s[l]) ?? 0) + 1);
            numNeeded += 1;
            l += 1;
        }
        // console.log(s.slice(l, r + 1));
    }

    return (minLeft !== -1) ? s.slice(minLeft, minLeft + minLength) : "";

};
