function topKFrequent(nums: number[], k: number): number[] {
    const count = new Map<number, number>();
    for (const num of nums) {
        count.set(num, (count.get(num) ?? 0) + 1)
    }

    const buckets: number[][] = Array.from(
    { length: nums.length + 1 },
    () => []
);

    for (const [num, freq] of count) {
        buckets[freq - 1].push(num);
    }

    const ans = new Array<number>();

    for (let i = buckets.length - 1; i >= 0; i--){
        const bucket = buckets[i];
        for (const num of bucket){
            ans.push(num);
        }
        if (ans.length === k) {
            return ans;
        }
    }
    
};
