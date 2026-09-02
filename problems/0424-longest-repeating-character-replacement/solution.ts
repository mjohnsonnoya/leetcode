function characterReplacement(s: string, k: number): number {
    const seen = new Map<string, number>();

    let l = 0;
    let maxLength = 0;
    let maxChar = 0;
    for (let r = 0; r < s.length; r++) {
        const rightChar= s[r];
        seen.set(rightChar, (seen.get(rightChar) ?? 0) + 1);

        maxChar = Math.max(maxChar, seen.get(rightChar));

        while ((r - l + 1) - maxChar > k) {
            const leftChar = s[l];
            seen.set(leftChar, seen.get(leftChar) - 1);
            l += 1;
        }

        maxLength = Math.max(maxLength, (r - l + 1));
    }
    
    return maxLength;
};
