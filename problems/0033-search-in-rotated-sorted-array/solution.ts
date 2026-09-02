function search(nums: number[], target: number): number {
    const n = nums.length;
    let l = 0;
    let r = n - 1;

    function binarySearch(start: number, end: number): number {
        let left = start;
        let right = end - 1;

        while (left <= right) {
            const m = Math.floor((left + right)/2);
            if (nums[m] === target) {
                return m;
            }

            else if (nums[m] > target) {
                right = m - 1;
            }

            else {
                left = m + 1;
            }
        }

        return -1;
    }

    while (l < r) {
        const m = Math.floor((l + r)/2);

        if (nums[r] < nums[m]) {
            l = m + 1;
        }
        
        else {
            r = m;
        }
    }

    console.log(l);

    // Select the correct sorted half based on target range
    if (target >= nums[l] && target <= nums[n - 1]) {
        return binarySearch(l, n);
    } else {
        return binarySearch(0, l);
    }
};
