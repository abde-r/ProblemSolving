class Solution {
    public boolean checkValid(int[][] matrix) {
        Set<String> s = new HashSet<>();
        int MATRIX_SIZE=matrix.length;
        
        for (int i=0; i<MATRIX_SIZE; i++) {
            for (int j=0; j<MATRIX_SIZE; j++)
                if (!s.add("R"+i+"_"+matrix[i][j]) || !s.add("C"+j+"_"+matrix[i][j]))
                    return false;
        }
        return true;
    }
}