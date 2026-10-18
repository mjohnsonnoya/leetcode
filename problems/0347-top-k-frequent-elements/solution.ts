function topKFrequent(nums: number[], k: number): number[] {
    const count = new Map<number, number>();
    for (const num of nums) {
        count.set(num, (count.get(num) ?? 0) + 1); 
    }

    const buckets = Array.from({length: nums.length + 1}, () => []);

    for (const [k, v] of count) {
        buckets[v].push(k);
    }

    let answer = [];
    for (let i = buckets.length - 1; i >= 0; i--) {
        for (const num of buckets[i]) {
            answer.push(num);
        }
        if (answer.length === k) {
            break;
        }
    }

    return answer;
};
