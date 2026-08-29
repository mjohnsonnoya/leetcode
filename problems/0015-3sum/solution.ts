function threeSum(nums: number[]): number[][] {
    const n = nums.length;
    nums.sort((a, b) => a - b);

    const ans: number[][] = [];

    for (let i = 0; i < n - 2; i++) {
        if (i > 0 && nums[i] === nums[i - 1]) {
            continue;
        }

        let l = i + 1;
        let r = n - 1;

        while (l < r) {
            const sum = nums[i] + nums[l] + nums[r];

            if (sum === 0) {
                ans.push([nums[i], nums[l], nums[r]]);

                l += 1;
                r -= 1;
                while (nums[l] === nums[l - 1] && l < r) {
                    l += 1;
                }
            }

            else if (sum > 0) {
                r -= 1;
            }

            else {
                l += 1;
            }
        }
    }

    return ans;
};
