class Solution {
    public int diagonalSum(int[][] mat) {
        int s1=0, s2=0;
        for (int i=0; i<mat.length; i++) {
            for (int j=0; j<mat[i].length; j++) {
                if (i==j)
                    s1+=mat[i][j];
                else if (mat[i].length-i-1==j)
                    s2+=mat[i][j];
            }
        }
        return s1+s2;
    }
}