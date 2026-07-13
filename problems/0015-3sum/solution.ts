function threeSum(nums: number[]): number[][] {
    
    nums.sort((a, b) => a - b);
    const ans: number[][] = new Array<number[]>();

    for (let i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] === nums[i-1]) {
            continue;
        }

        let l = i + 1;
        let r = nums.length - 1;

        while (l < r){
            const sum = nums[i] + nums[l] + nums[r];

            if (sum === 0){
                ans.push([nums[i], nums[l], nums[r]]);
                l += 1;
                r -= 1;
                while (nums[l] === nums[l - 1]) {
                    l += 1;
                }
            }

            if (sum < 0) {
                l += 1;
            }

            if (sum > 0) {
                r -= 1;
            }
        }

    }
    return ans;
    
};
