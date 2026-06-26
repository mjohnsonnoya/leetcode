function isValidSudoku(board: string[][]): boolean {
    const nrows = board.length;
    const ncols = board[0].length;

    // Check rows
    for (const row of board) {
        const seen = new Set<string>();

        for (const value of row) {
            if (value === ".") continue;

            if (seen.has(value)) {
                return false;
            }

            seen.add(value);
        }
    }

    // Check columns
    for (let col = 0; col < ncols; col++) {
        const seen = new Set<string>();

        for (let row = 0; row < nrows; row++) {
            const value = board[row][col];

            if (value === ".") continue;

            if (seen.has(value)) {
                return false;
            }

            seen.add(value);
        }
    }

    // Check 3×3 boxes
    for (let boxRow = 0; boxRow < 9; boxRow += 3) {
        for (let boxCol = 0; boxCol < 9; boxCol += 3) {
            const seen = new Set<string>();

            for (let row = boxRow; row < boxRow + 3; row++) {
                for (let col = boxCol; col < boxCol + 3; col++) {
                    const value = board[row][col];

                    if (value === ".") continue;

                    if (seen.has(value)) {
                        return false;
                    }

                    seen.add(value);
                }
            }
        }
    }

    return true;
}
