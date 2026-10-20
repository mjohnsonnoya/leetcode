function search(nums: number[], target: number): number {
    let l = 0;
    const n = nums.length;
    let r = n - 1;

    while (l < r) {
        const m = Math.floor((l + r) / 2);
        if (nums[m] < nums[r]) {
            r = m;
        }

        else {
            l = m + 1;
        }
    }

    function binarySearch(start: number, end: number) {
        let left = start;
        let right = end;

        while (left <= right) {
            const middle = Math.floor((left + right)/2);

            if (nums[middle] === target) {
                return middle;
            }

            else if (nums[middle] > target) {
                right = middle - 1;
            }

            else {
                left = middle + 1;
            }
        }

        return -1;
    }

    const val1 = binarySearch(0, l-1);
    const val2 = binarySearch(l, n - 1);

    return (val1 !== -1) ? val1 : val2;
};
