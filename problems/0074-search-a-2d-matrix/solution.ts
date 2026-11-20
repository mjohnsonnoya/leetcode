function searchMatrix(matrix: number[][], target: number): boolean {
    const m = matrix.length;
    const n = matrix[0].length;

    let left = 0;
    let right = m - 1;

    while (left < right) {
        const middle = Math.ceil((left + right)/2);
        if (target <= matrix[middle][n - 1] && target >= matrix[middle][0]) {
            left = middle;
            right = middle;
        }

        if (target > matrix[middle][n - 1]) {
            left = middle + 1;
        }

        else if (target < matrix[middle][0]) {
            right = middle - 1;
        }
    }

    if (left > m - 1 || right < 0) return false;

    const row = left;

    let l = 0;
    let r = n - 1;

    while (l <= r) {
        const m = Math.floor((l + r)/2);

        if (target === matrix[row][m]) {
            return true;
        }

        else if (target > matrix[row][m]) {
            l = m + 1;
        }

        else {
            r = m - 1;
        }
    }

    return false;
};
