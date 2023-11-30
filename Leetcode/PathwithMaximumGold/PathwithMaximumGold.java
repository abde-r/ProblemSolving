class Solution {

    private int getGold(int[][] grid, int i, int j, int m, int n, boolean[][] visited) {
        int right, left, up, down;
        if (i<0 || i>=m || j<0 || j>=n || grid[i][j] == 0 || visited[i][j])
            return 0;
        visited[i][j] = true;
        right = getGold(grid, i, j+1, m, n, visited);
        left = getGold(grid, i, j-1, m, n, visited);
        up = getGold(grid, i-1, j, m, n, visited);
        down = getGold(grid, i+1, j, m, n, visited);
        visited[i][j] = false;
        return Math.max(right, Math.max(left, Math.max(up, down)))+grid[i][j];
    }

    public int getMaximumGold(int[][] grid) {

        int maxGold=0, m=grid.length, n=grid[0].length;
        if (grid.length==0)
            return 0;
        
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (grid[i][j]>0) {
                    int gold = getGold(grid, i, j, m, n, new boolean[m][n]);
                    maxGold = Math.max(maxGold, gold);
                }
            }
        }
        return maxGold;
    }
}