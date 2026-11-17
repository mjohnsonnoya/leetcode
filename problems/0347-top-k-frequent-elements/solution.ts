function topKFrequent(nums: number[], k: number): number[] {
    const counter = new Map<number, number>();

    for (const num of nums) {
        counter.set(num, (counter.get(num) ?? 0) + 1);
    }

    const buckets = Array.from({length: nums.length + 1}, () => []);

    for (const [num, count] of counter) {
        buckets[count].push(num);
    }

    const answer = [];

    for (let i = buckets.length - 1; i >= 0; i--) {
        for (let j = 0; j < buckets[i].length; j++) {
            answer.push(buckets[i][j]);
        }
        if (answer.length === k) {
            return answer;
        }
    }
};
