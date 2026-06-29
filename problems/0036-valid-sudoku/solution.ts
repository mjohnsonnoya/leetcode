function isValidSudoku(board: string[][]): boolean {
    const nrows = board.length;
    const ncols = board[0].length;
    
     // check rows
    for (let row = 0; row < nrows; row++){
        const seen = new Set<string>();
        for (let col = 0; col < ncols; col++){
            const val = board[row][col];
            if (val !== '.' && seen.has(val)) {
                return false;
            }
            seen.add(val);
        }
        
    }
    
    // check cols
    for (let col = 0; col < ncols; col++){
        const seen = new Set<string>();
        for (let row = 0; row < nrows; row++){
            const val = board[row][col];
            if (val !== '.' && seen.has(val)) {
                return false;
            }
            seen.add(val);
        }
    }
    
    // check the squares
    for (let row = 0; row < nrows; row += 3){
        for (let col = 0; col < ncols; col += 3){
            const seen = new Set<string>();
            for (let r = row; r < row + 3; r++){
                for (let c = col; c < col + 3; c ++) {
                    const val = board[r][c];
                    if (val !== '.' && seen.has(val)) {
                return false;
            }
            seen.add(val);
                }
            }
        }
    }
    return true;
    
};
