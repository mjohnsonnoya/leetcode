function twoSum(nums: number[], target: number): number[] {
    const seen = new Map<number, number>();
    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        const resid = target - num;
        if (seen.has(resid)){
            return [seen.get(resid), i];
        }
        seen.set(num, i);
    }
    return [-1,-1];
};
