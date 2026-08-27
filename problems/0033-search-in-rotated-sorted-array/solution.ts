function search(nums: number[], target: number): number {

    function binarySearch(start: number, end: number) {
        let left = start;
        let right = end - 1;

        while (left <= right) {
            const m = Math.floor((left + right) / 2);

            if (nums[m] == target) {
                return m;
            }

            if (nums[m] < target) {
                left = m + 1;
            }

            else {
                right = m - 1;
            }
        }

        return -1;
    }
    
    let l = 0;
    let r = nums.length - 1;

    while (l < r) {
        const m = Math.floor((l + r)/2);

        if (nums[r] < nums[m]) {
            l = m + 1;
        }

        else {
            r = m;
        }
    }

    const k1 = binarySearch(0, l);
    const k2 = binarySearch(l, nums.length);

    return (k1 !== -1) ? k1 : k2;
};
