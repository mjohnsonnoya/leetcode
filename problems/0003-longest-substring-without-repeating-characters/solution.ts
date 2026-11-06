function lengthOfLongestSubstring(s: string): number {

    const seen = new Set();
    let maxLength = 0;
    
    let l = 0;
    for (let r = 0; r < s.length; r++) {
        const rightChar = s[r];

        while (seen.has(rightChar)) {
            const leftChar = s[l];
            seen.delete(leftChar);
            l += 1;
        }

        seen.add(rightChar);
        maxLength = Math.max(maxLength, seen.size);
    }

    return maxLength;
};
