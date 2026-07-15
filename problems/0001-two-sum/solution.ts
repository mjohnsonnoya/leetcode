function twoSum(nums: number[], target: number): number[] {
    const seen = new Map<number, number>();

    for (let i = 0; i < nums.length; i++) {
        const num: number = nums[i];
        const res = target - num;
        if (seen.has(res)) {
            return [i, seen.get(res)];
        }
        seen.set(num, i);
    }
};
