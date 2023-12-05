class Solution {
    private int GRID_SIZE = 9;
    private boolean isNumberInRow(char[][] board, int row, char n) {
        for (int i=0; i<GRID_SIZE; i++)
            if (board[row][i]==n)
                return true;
        return false;
    }

    private boolean isNumberInColumn(char[][] board, int column, char n) {
        for (int i=0; i<GRID_SIZE; i++)
            if (board[i][column]==n)
                return true;
        return false;
    }

    private boolean isNumberInBox(char[][] board, int row, int column, char n) {
        int localBoxRow = row-row%3;
        int localBoxColumn = column-column%3;

        for (int i=localBoxRow; i<localBoxRow+3; i++) {
            for (int j=localBoxColumn; j<localBoxColumn+3; j++) {
                if (board[i][j]==n)
                    return true;
            }
        }
        return false;
    }

    private boolean isValidPlacement(char[][] board, int row, int column, char n) {
        return !isNumberInRow(board, row, n) && !isNumberInColumn(board, column, n) && !isNumberInBox(board, row, column, n);
    }

    private boolean solveBoard(char[][] board) {
        for (int row=0; row<GRID_SIZE; row++) {
            for (int column=0; column<GRID_SIZE; column++) {
                if (board[row][column]=='.') {
                    for (int numberToTry=1; numberToTry<=GRID_SIZE; numberToTry++) {
                        if (isValidPlacement(board, row, column, Character.forDigit(numberToTry, 10))) {
                            board[row][column]=Character.forDigit(numberToTry, 10);
                            if (solveBoard(board))
                                return true;
                            else
                                board[row][column]='.';
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }

    public void solveSudoku(char[][] board) {
        solveBoard(board);

    }
}