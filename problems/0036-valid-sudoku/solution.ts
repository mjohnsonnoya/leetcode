function isValidSudoku(board: string[][]): boolean {
    const nrows = board.length;
    const ncols = board[0].length;
    
    // check the rows
    for (let r = 0; r < nrows; r++) {
        const seen = new Set();
        for (let c = 0; c < ncols; c++) {
            const val = board[r][c];
            if (val === '.') {
                continue;
            }

            if (seen.has(val)) {
                return false;
            }

            seen.add(val);
        }
    }

    // check the cols
    for (let c = 0; c < ncols; c++) {
        const seen = new Set();
        for (let r = 0; r < nrows; r++) {
            const val = board[r][c];
            if (val === '.') {
                continue;
            }

            if (seen.has(val)) {
                return false;
            }

            seen.add(val);
        }
    }

    // check the squares
    for (let row = 0; row < nrows; row += 3) {
        for (let col = 0; col < ncols; col += 3) {
            const seen = new Set();
            for (let r = row; r < row + 3; r++) {
                for (let c = col; c < col + 3; c++) {
                    const val = board[r][c];
                    if (val === '.') {
                        continue;
                    }

                    if (seen.has(val)) {
                        return false;
                    }

                    seen.add(val);
                }
            }
        }
    }

    return true;
};
