function productExceptSelf(nums: number[]): number[] {
    let suffix = 1;
    let prefix = 1;
    const ans: number[] = new Array(nums.length).fill(1);

    for (let i = 0; i < nums.length; i++){
        const j = nums.length - i - 1
        ans[i] *= prefix;
        ans[j] *= suffix;

        prefix *= nums[i];
        suffix *= nums[j];
    }
    return ans;
};
