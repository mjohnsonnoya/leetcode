function topKFrequent(nums: number[], k: number): number[] {
    const count = new Map<number, number>();

    for (const num of nums) {
        count.set(num, (count.get(num) ?? 0) + 1);
    }

    const buckets: number[][] = Array.from({length: nums.length + 1}, () => []);

    for (const [num, freq] of count) {
        buckets[freq].push(num);
    }

    const ans: number[] = [];

    for (let idx = buckets.length - 1; idx >= 0; idx--) {
        for (const num of buckets[idx]) {
            ans.push(num)
        }

        if (ans.length === k) {
            break;
        }
    }

    return ans;
};
