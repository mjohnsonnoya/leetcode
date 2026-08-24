function search(nums: number[], target: number): number {
    const n = nums.length;
    let l = 0;
    let r = n - 1;

    function binarySearch(start: number, end: number): number {
        let left = start;
        let right = end - 1;

        while (left <= right) {
            const middle = Math.floor((left + right) / 2);
            if (nums[middle] === target) {
                return middle;
            }

            else if (nums[middle] < target) {
                left = middle + 1;
            }

            else {
                right = middle - 1;
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

    const k1 = binarySearch(l, n);
    const k2 = binarySearch(0, l);


    if (k1 !== -1) {
        return k1;
    }

    if (k2 !== -1) {
        return k2;
    }

    return -1;
};
