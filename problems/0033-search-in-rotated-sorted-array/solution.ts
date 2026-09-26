function search(nums: number[], target: number): number {
    let l = 0;
    let r = nums.length - 1;

    function binarySearch(left: number, right: number): number {
        let l = left;
        let r = right - 1;

        while (l <= r) {
            const m = Math.floor((l + r)/2);

            if (nums[m] === target) {
                return m;
            }

            else if (nums[m] < target) {
                l = m + 1;
            }

            else {
                r = m - 1;
            }
        }

        return -1;
    }

    while (l < r) {
        const m = Math.floor((l + r)/2);

        if (nums[m] > nums[r]) {
            l = m + 1;
        }

        else {
            r = m;
        }
    }

    const pivot = l;

    if (target >= nums[pivot] && target <= nums[nums.length - 1]) {
        return binarySearch(pivot, nums.length);
    }

    else {
        return binarySearch(0, pivot);
    }

};
