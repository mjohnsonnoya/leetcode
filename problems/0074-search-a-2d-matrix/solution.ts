function searchMatrix(matrix: number[][], target: number): boolean {
    const numRows = matrix.length;
    const numCols = matrix[0].length;

    let leftRow = 0;
    let rightRow = numRows - 1;

    let middleRow = -1;

    while (leftRow <= rightRow) {
        middleRow = Math.floor((leftRow + rightRow) / 2);

        if (target <= matrix[middleRow][numCols - 1] && target >= matrix[middleRow][0]) {
            break;
        }

        else if (target > matrix[middleRow][numCols - 1]) {
            leftRow = middleRow + 1;
        }

        else {
            rightRow = middleRow - 1;
        }
    }

    if (middleRow === -1) {
        return false;
    }

    const row = matrix[middleRow];

    let l = 0;
    let r = numCols - 1;

    while (l <= r) {
        const m = Math.floor((l + r) / 2);

        if (target === row[m]) {
            return true;
        }

        else if (target > row[m]) {
            l = m + 1;
        }

        else {
            r = m - 1;
        }
    }

    return false;
};
