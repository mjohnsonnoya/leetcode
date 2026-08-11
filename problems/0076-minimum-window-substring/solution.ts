function minWindow(s: string, t: string): string {
    if (t.length > s.length) {
        return "";
    }

    let numNeeded = t.length;
    const need = new Map<string, number>();

    for (const c of t) {
        need.set(c, (need.get(c) ?? 0) + 1);
    }

    let l = 0;
    let leftMax = -1;
    let minLength = Infinity;

    for (let r = 0; r < s.length; r++) {
        if (need.has(s[r])) {
            if (need.get(s[r]) > 0) {
                numNeeded -= 1;
            }
            need.set(s[r], need.get(s[r]) - 1);
        }

        if (numNeeded === 0) {
            while ((!need.has(s[l])) || need.get(s[l]) < 0) {
                if (need.has(s[l])) {
                    need.set(s[l], need.get(s[l]) + 1);
                }
                l += 1;
            }

            if ((r - l + 1) < minLength) {
                leftMax = l;
                minLength = (r - l + 1);
            }
        }
    }

    return (leftMax === -1) ? "" : s.slice(leftMax, leftMax + minLength);
};
