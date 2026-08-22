function lengthOfLongestSubstring(s: string): number {
    const n = s.length;

    const substring = new Set<string>();

    let maxLength = 0;
    let l = 0;

    for (let r = 0; r < n; r++) {
        while (substring.has(s[r])) {
            substring.delete(s[l]);
            l += 1;
        }

        substring.add(s[r]);
        if ((r - l + 1) >= maxLength) {
            maxLength = r - l + 1;
        }


    }

    return maxLength;
};
