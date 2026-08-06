function minWindow(s: string, t: string): string {
    const needed = new Map<string, number>();
    let numNeeded = t.length;

    for (const c of t) {
        needed.set(c, (needed.get(c) ?? 0) + 1);
    }

    let l = 0;

    let leftMin = -1;
    let minLength = Infinity;

    for (let r = 0; r < s.length; r++) {
        if (needed.has(s[r])) {
            if (needed.get(s[r]) > 0) {
                 numNeeded -= 1;
            }
            needed.set(s[r], needed.get(s[r]) - 1);
        }

        if (numNeeded === 0) {
            while (!needed.has(s[l]) || needed.get(s[l]) < 0) {
                if (needed.has(s[l])) {
                    needed.set(s[l], needed.get(s[l]) + 1);
                }

                l += 1;
            }

            if ((r - l + 1) < minLength) {
                minLength = (r - l + 1);
                leftMin = l;
            }

        }
    }

    return (leftMin === -1) ? "" : s.slice(leftMin, leftMin + minLength);
};
