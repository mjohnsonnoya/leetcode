function groupAnagrams(strs: string[]): string[][] {
    const groups = new Map<string, string[]>();

    for (const word of strs) {
        const count: number[] = new Array(26).fill(0);
        for (const c of word) {
            count[c.charCodeAt(0) - 'a'.charCodeAt(0)]++;
        }

        const key = count.join(',');
        
        const words: string[] = groups.get(key) ?? [];
        words.push(word);
        groups.set(key, words);
    }

    const ans: string[][] = [];

    for (const group of groups.values()) {
        ans.push(group);
    }

    return ans;

};
