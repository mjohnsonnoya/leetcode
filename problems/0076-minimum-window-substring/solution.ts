function minWindow(s: string, t: string): string {
    let neededCount = t.length;
    const need = new Map<string, number>();

    for (const char of t) {
        need.set(char, (need.get(char) ?? 0) + 1);
    }

    let leftMin = -1;
    let minLength = Infinity;

    let l = 0;

    for (let r = 0; r < s.length; r++) {
        if (need.has(s[r])) {
            if (need.get(s[r]) > 0) {
                neededCount -= 1;
            }
            need.set(s[r], need.get(s[r]) - 1);
        }

        if (neededCount === 0) {
            while (need.get(s[l]) < 0 || !need.has(s[l])) {
                if (need.has(s[l])) {
                     need.set(s[l], need.get(s[l]) + 1);
                }
                l += 1;
            }

            if ((r - l + 1) < minLength) {
                leftMin = l;
                minLength = (r - l) + 1;
            }
            neededCount += 1;
            need.set(s[l], need.get(s[l]) + 1);
            l += 1;
        }
    }

    return leftMin === -1 ? "" : s.slice(leftMin, leftMin + minLength);
};
