function minWindow(s: string, t: string): string {
    const count = new Map<string, number>();
    for (const c of t) {
        count.set(c, (count.get(c) ?? 0) + 1);
    }

    let numNeeded = t.length;
    let l = 0;
    let leftMin = -1;
    let minLength = Infinity;


    for (let r = 0; r < s.length; r++) {
        
        if (count.has(s[r])) {
            if (count.get(s[r]) > 0) {
                numNeeded -= 1;
            }
            count.set(s[r], count.get(s[r]) - 1);
        }


        if (numNeeded === 0) {
            while(count.get(s[l]) < 0 || !count.has(s[l])) {
                if (count.has(s[l])) {
                    count.set(s[l], count.get(s[l]) + 1);
                }
                l += 1;
            }

            if ((r - l + 1) < minLength) {
                leftMin = l;
                minLength = (r - l + 1);
            }
            count.set(s[l], count.get(s[l]) + 1);
            numNeeded += 1;
            l += 1;
        }
    }

    return (leftMin === -1) ? "" : s.slice(leftMin, leftMin + minLength);
};
