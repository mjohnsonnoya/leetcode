function topKFrequent(nums: number[], k: number): number[] {
    const freqs = new Map<number, number>();
    for (const num of nums) {
        freqs.set(num, (freqs.get(num) ?? 0) + 1);
    }

    const buckets: number[][] = Array.from({length: nums.length + 1}, () => []);


    for (const [num, freq] of freqs) {
        buckets[freq].push(num);
    }

    const ans = new Array<number>();
    
    for (let i = buckets.length - 1; i >= 0; i --) {
        for (const num of buckets[i]) {
            ans.push(num);
        }
        if (ans.length === k) {
            return ans;
        }
    }
    
};
