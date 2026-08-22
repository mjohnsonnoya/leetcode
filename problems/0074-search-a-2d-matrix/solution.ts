function searchMatrix(matrix: number[][], target: number): boolean {
    const nrows = matrix.length;
    const ncols = matrix[0].length;

    let leftRow = 0;
    let rightRow = nrows - 1;
    let middleRow = -1;

    while (leftRow <= rightRow) {
        middleRow = Math.floor((leftRow + rightRow) / 2);
        if (target >= matrix[middleRow][0] && target <= matrix[middleRow][ncols - 1]) {
            let l = 0;
            let r = ncols - 1;
            while (l <= r) {
                const m = Math.floor((l + r) / 2);
                if (matrix[middleRow][m] === target) {
                    return true;
                }

                else if (target > matrix[middleRow][m]) {
                    l = m + 1;
                }

                else {
                    r = m - 1;
                }
            }

            return false;
        }

        else if (target > matrix[middleRow][ncols - 1]) {
            leftRow = middleRow + 1;
        }

        else {
            rightRow = middleRow - 1;
        }
    }

    return false;
};
