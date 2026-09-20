function searchMatrix(matrix: number[][], target: number): boolean {
    const nrows = matrix.length;
    const ncols = matrix[0].length;

    let left = 0;
    let right = nrows - 1;

    while (left < right) {
        const middle = Math.ceil((left + right)/2);

        if (target < matrix[middle][0]) {
            right = middle - 1;
        }

        else {
            left = middle;
        }
    }

    if (left < 0 || right > nrows - 1) {
        return false;
    }

    const row = left;

    let l = 0;
    let r = ncols - 1;

    while (l <= r) {
        const m = Math.floor((l + r) / 2);

        if (matrix[row][m] === target) {
            return true;
        }

        else if (matrix[row][m] < target) {
            l = m + 1;
        }

        else {
            r = m - 1;
        }
    }

    return false;
};
