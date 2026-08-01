function lengthOfLongestSubstring(s: string): number {
    let l = 0
    const count = new Map<string, number>();
    
    let maxLength = 0;

    for (let r = 0; r < s.length; r++) {
        count.set(s[r], (count.get(s[r]) ?? 0) + 1);

        while (count.get(s[r]) > 1) {
            count.set(s[l], count.get(s[l]) - 1);
            l += 1; 
        }

        maxLength = Math.max(maxLength, (r - l + 1));
    }

    return maxLength;
};
