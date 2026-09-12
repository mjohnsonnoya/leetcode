function isValidSudoku(board: string[][]): boolean {
    const nrows = board.length;
    const ncols = board[0].length;
    
    // check the rows
    for (let row = 0; row < nrows; row++) {
        const seen = new Set<string>();
        for (let col = 0; col < ncols; col++) {
            const value = board[row][col];
            if (value === ".") {
                continue;
            }
            if (seen.has(value)) {
                return false; 
            }
            seen.add(value);
        }
    }


    // check the cols
    for (let col = 0; col < ncols; col++) {
        const seen = new Set<string>();
        for (let row = 0; row < nrows; row++) {
            const value = board[row][col];
            if (value === ".") {
                continue;
            }

            if (seen.has(value)) {
                return false;
            }

            seen.add(value);
        }
    }

    // check the "squares"
    for (let r = 0; r < nrows; r += 3) {
        for (let c = 0; c < ncols; c += 3) {
            const seen = new Set<string>();
            for (let row = r; row < r + 3; row++) {
                for (let col = c; col < c + 3; col++) {
                    const value = board[row][col];
                    if (value === ".") {
                        continue;
                    }

                    if (seen.has(value)) {
                        return false;
                    }

                    seen.add(value);
                }
            }
        }
    }

    return true;

};
