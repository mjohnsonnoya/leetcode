function lengthOfLongestSubstring(s: string): number {
    let l = 0;
    let r = 0;
    let maxLength = 0;
    const substring = new Set<string>();

    while (r < s.length) {
        while (substring.has(s[r])) {
            substring.delete(s[l]);
            l += 1;
        }

        substring.add(s[r]);
        if (substring.size > maxLength) {
            maxLength = substring.size;
        }

        r += 1;
    }

    return maxLength;
};
