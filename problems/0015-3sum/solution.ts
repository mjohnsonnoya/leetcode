function threeSum(nums: number[]): number[][] {
    nums.sort((a, b) => a - b);

    const ans: [number, number, number][] = [];

    for (let i = 0; i < nums.length - 2; i++) {
        if (i !== 0 && nums[i] === nums[i - 1]) {
            continue;
        }
        let j = i + 1;
        let k = nums.length - 1;
        while (j < k) {
            const sum = nums[i] + nums[j] + nums[k];

            if (sum === 0) {
                ans.push([nums[i], nums[j], nums[k]]);
                j += 1;
                k -= 1;

                while (nums[j] === nums[j - 1]) {
                    j += 1;
                }
            }

            else if (sum > 0) {
                k -= 1;
            }

            else {
                j += 1;
            }
         }
    }

    return ans;
};
