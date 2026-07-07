function isValidSudoku(board: string[][]): boolean {
    const nrows = board.length;
    const ncols = board.length;

    // check the rows
    for (let row = 0; row < nrows; row++){
        const seen = new Set<string>();
        for (let col = 0; col < ncols; col++) {
            const val = board[row][col];
            if (val === '.') {
                continue;
            }
            else if (seen.has(val)) {
                return false;
            }
            else {
                seen.add(val);
            }
        }
    }

    // check the cols
    for (let col = 0; col < ncols; col++){
        const seen = new Set<string>();
        for (let row = 0; row < nrows; row++){
            const val = board[row][col];
            if (val === '.') {
                continue;
            }
            else if (seen.has(val)) {
                
                return false;
            }
            else {
                seen.add(val);
            }
        }
    }

    // check the boxes
    for (let row = 0; row < nrows; row+=3){
        for (let col = 0; col < ncols; col += 3){
            const seen = new Set<string>();
            for (let r = row; r < row + 3; r++){
                for (let c = col; c < col + 3; c++){
                    const val = board[r][c];
                    if (val === '.') {
                        continue;
                    }
                    else if (seen.has(val)) {
                        return false;
                    }
                    else {
                        seen.add(val);
                    }
                }
            }
        }
    }
    return true;
};
