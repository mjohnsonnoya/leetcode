function groupAnagrams(strs: string[]): string[][] {
    const groups = new Map<string, string[]>();
    const aCharCode = 'a'.charCodeAt(0);

    for (const word of strs) {
        const count: number[] = Array<number>(26).fill(0);
        for (let i = 0; i < word.length; i++) {
            const idx = word.charCodeAt(i) - aCharCode;
            count[idx] += 1;
        }
        const key = count.join(',');
        if (!groups.has(key)) {
            groups.set(key, []);
        }

        groups.get(key).push(word);
    }

    return [...groups.values()];
};
