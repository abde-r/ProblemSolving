class Solution {
    private int captureRegion(char[][] board, int i, int j, int m, int n) {
        if (i>=0 && i<m && j>=0 && j<n && board[i][j]=='O') {
            board[i][j] = 'A';
            captureRegion(board, i, j+1, m, n);
            captureRegion(board, i, j-1, m, n);
            captureRegion(board, i+1, j, m, n);
            captureRegion(board, i-1, j, m, n);
        }
        return 1;
    }

    public void solve(char[][] board) {
        int islands = 0, m=board.length, n=board[0].length;

        if (m<=2 || n<=2)
            return;
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++)
                if (board[i][j] == 'O' && (i==0 || i==m-1 || j==0 || j==n-1))
                    captureRegion(board, i, j, m, n);
        }

        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++)
                if (board[i][j] == 'O')
                    board[i][j] = 'X';
                else if (board[i][j] == 'A')
                    board[i][j] = 'O';
        }
    }
}