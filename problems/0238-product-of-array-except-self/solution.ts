function productExceptSelf(nums: number[]): number[] {
    const ans = new Array<number>(nums.length).fill(1);
    const n = nums.length;

    let prefix = 1;
    let suffix = 1;
    
    for (let i = 0; i < nums.length; i++) {
        ans[i] *= prefix;
        ans[n - i - 1] *= suffix;

        prefix *= nums[i];
        suffix *= nums[n - i - 1];
    }

    return ans;
};
