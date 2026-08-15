function threeSum(nums: number[]): number[][] {
    nums.sort((a, b) => a - b);
    const ans: number[][] = [];

    for (let i = 0; i < nums.length; i++) {
        let l = i + 1;
        let r = nums.length - 1;

        if (i > 0 && nums[i] === nums[i - 1]) {
            continue;
        }
        while (l < r) {
            let total = nums[i] + nums[l] + nums[r];
            if (total === 0) {
                ans.push([nums[i], nums[l], nums[r]]);
                l += 1;
                r -= 1;
                while (nums[l] === nums[l - 1] && l < r) {
                    l += 1;
                }
            }

            else if (total > 0) {
                r -= 1;
            }

            else {
                l += 1;
            }
        }
    }

    return ans;
};
