function findMin(nums: number[]): number {
    const n = nums.length;
    let l = 0.
    let r = n - 1;

    while (l < r) {
        const m = Math.floor((l + r)/2);
        if (nums[r] < nums[m]) {
            l = m + 1;
        }
        else {
            r = m;
        }
    }

    return nums[l];
};
