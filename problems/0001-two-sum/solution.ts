function twoSum(nums: number[], target: number): number[] {
    const seen = new Map<number, number>;
    
    for (let i = 0; i < nums.length; i++) {
        const val = nums[i];
        const resid = target - val;
        if (seen.has(resid)) {
            return Array<number>(i, seen.get(resid));
        }
        seen.set(val, i);
    }
};
