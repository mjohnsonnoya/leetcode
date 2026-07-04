function groupAnagrams(strs: string[]): string[][] {
    const buckets = new Map<string, string[]>();

    for (const word of strs) {
        const count = new Array<number>(26).fill(0);
        for (let i = 0; i < word.length; i++) {
            count[word.charCodeAt(i) - 'a'.charCodeAt(0)]++;
        }
        const key = count.join(',');
        if (!buckets.has(key)){
            buckets.set(key, []);
        }

        buckets!.get(key).push(word);
    }

    return [...buckets.values()];
};
