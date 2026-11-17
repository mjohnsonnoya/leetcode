function search(nums: number[], target: number): number {
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

    const pivot = l;

    function binarySearch(left: number, right: number): number {
        while (left <= right) {
            const middle = Math.floor((left + right)/2);

            if (nums[middle] === target) {
                return middle;
            }

            else if (nums[middle] > target) {
                right = middle - 1
            }

            else {
                left = middle + 1;
            }
        }

        return -1;
    }

    if (target >= nums[pivot] && target <= nums[nums.length - 1]) {
        return binarySearch(pivot, nums.length - 1);
    }

    else return binarySearch(0, pivot - 1);
};
