function twoSum(numbers: number[], target: number): number[] {
    let l = 0;
    let r = numbers.length - 1;

    while (l < r) {
        const sum = numbers[l] + numbers[r];
        let resid = sum - target;
        if (resid === 0) {
            return [l + 1, r + 1];
        }

        else if (resid > 0) {
            r -= 1;
        }

        else {
            l += 1;
        }
    }
};
