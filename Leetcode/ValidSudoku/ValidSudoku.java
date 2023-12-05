class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<String> s = new HashSet<>();
        int BOARD_SIZE=9;
        
        for (int i=0; i<BOARD_SIZE; i++) {
            for (int j=0; j<BOARD_SIZE; j++) {
                char c = board[i][j];
                if (c!='.')
                    if (!s.add("R"+i+c) || !s.add("C"+j+c) || !s.add("G"+c+i/3+j/3))
                        return false;
            }
        }
        return true;
    }
}