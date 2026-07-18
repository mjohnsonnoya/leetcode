function isValidSudoku(board: string[][]): boolean {
    const nrows = board.length;
    const ncols = board[0].length;
    
    // check all the rows
    for (let row = 0; row < nrows; row++) {
        const seen = new Set<string>();
        for (let col = 0; col < ncols; col++) {
            if (board[row][col] === '.') {
                continue;
            }
            else if (seen.has(board[row][col])) {
                return false;
            }

            else {
                seen.add(board[row][col]);
            }
        }
    }

    // check all the cols
    for (let col = 0; col < ncols; col++) {
        const seen = new Set<string>();
        for (let row = 0; row < nrows; row++) {
            if (board[row][col] === '.') {
                continue;
            }
            else if (seen.has(board[row][col])) {
                console.log(board[row][col]);
                console.log(row);
                console.log(col);
                return false;
            }

            else {
                seen.add(board[row][col]);
            }
        }
    }

    // check all the boxes
    for (let row = 0; row < nrows; row += 3) {
        for (let col = 0; col < ncols; col += 3) {
            const seen = new Set<string>();
            for (let r = row; r < row + 3; r++) {
                for (let c = col; c < col + 3; c++) {
                    if (board[r][c] === '.') {
                        continue;
                    }
                    else if (seen.has(board[r][c])) {
                        return false;
                    }

                    else {
                        seen.add(board[r][c]);
                    }
                }
            }
        }
    }

    return true;


};
