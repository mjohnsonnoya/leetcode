function repeatedSubstringPattern(s: string): boolean {
    for (let r = 0; r < s.length; r++) {
        const substring = s.slice(0, r);
        if (s.length % substring.length !== 0) {
            continue
        }

        let valid = true;

        for (let i = 0; i < s.length/substring.length; i++) {
            if (substring !== s.slice(i * substring.length, (i + 1) * substring.length)) {
                valid = false;
            } 
        }
        if (valid === true) { return true; }
    }
    return false;
};
