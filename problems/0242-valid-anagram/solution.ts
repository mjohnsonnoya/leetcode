function isAnagram(s: string, t: string): boolean {
    if (t.length !== s.length) {
        return false;
    }
    const count: number[] = new Array<number>(26).fill(0);

    const aCharCode = 'a'.charCodeAt(0);

    for (let i = 0; i < s.length; i++) {
        count[s.charCodeAt(i) - aCharCode]++;
        count[t.charCodeAt(i) - aCharCode]--;
    }

    for (const num of count) {
        if (num !== 0) {
            return false;
        }
    }

    return true;

};
