function search(nums: number[], target: number): number {
    const n = nums.length;
    
    let l = 0;
    let r = n - 1;

    while (l < r) {
        const m = Math.floor((l + r) / 2);

        if (nums[m] > nums[r]) {
            l = m + 1;
        }

        else {
            r = m;
        }
    }

    function binarySearch(start: number, end: number){
        let left = start;
        let right = end - 1;
        while (left <= right) {
            const middle = Math.floor((left + right)/2);
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

        return - 1;
    }

    return (nums[0] <= target && target <= nums[l - 1]) ? binarySearch(0, l) : binarySearch(l, n);
};
