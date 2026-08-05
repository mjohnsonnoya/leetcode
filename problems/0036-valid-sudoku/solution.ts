function isValidSudoku(board: string[][]): boolean {
    const nrows = board.length;
    const ncols = board[0].length;
    
    // check the rows
    for (let r = 0; r < nrows; r++) {
        const seen = new Set<string>();
        for (let c = 0; c < ncols; c++) {
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

    // check columns
    for (let c = 0; c < ncols; c++) {
        const seen = new Set<string>();
        for (let r = 0; r < nrows; r++) {
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

    // check the boxes
    for (let r = 0; r < nrows; r += 3) {
        for (let c = 0; c < ncols; c += 3) {
            const seen = new Set<string>();
            for (let row = r; row < r + 3; row++ ) {
                for (let col = c; col < c + 3; col++ ) {
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
        }
    }

    return true;
    
};
