function productExceptSelf(nums: number[]): number[] {
    const ans = new Array<number>(nums.length).fill(1);

    let prev = 1;
    let post = 1;

    for (let i = 0; i < nums.length; i++) {
        const j = nums.length - i - 1;

        ans[i] *= prev;
        ans[j] *= post;

        prev *= nums[i];
        post *= nums[j];
    }

    return ans;
};
