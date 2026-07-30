function minWindow(s: string, t: string): string {
    if (t === "" || t.length > s.length) {
        return "";
    }

    const needed = new Map<string, number>();
    let numNeeded = 0;
    for (const c of t) {
        needed.set(c, (needed.get(c) ?? 0) + 1);
        numNeeded += 1;
    }
    let l = 0;
    let minLeft = -1;
    let minLength = Infinity;

    for (let r = 0; r < s.length; r++) {
        if (needed.has(s[r])) {
            if (needed.get(s[r]) > 0) {
                numNeeded -= 1;
            }
            needed.set(s[r], needed.get(s[r]) - 1);
        }

        if (numNeeded === 0) {
            while (needed.get(s[l]) < 0 || !needed.has(s[l])) {
                if (needed.has(s[l])) {
                    needed.set(s[l], needed.get(s[l]) + 1);
                }
                l += 1;
            }
            const length = (r - l + 1);
            if (length < minLength) {
                minLength = length;
                minLeft = l;
            }

            needed.set(s[l], 1);
            numNeeded += 1;
            l += 1;
        }
    }

     return (minLeft !== -1) ? s.slice(minLeft, minLeft + minLength) : "";
};
