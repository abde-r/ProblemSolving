class Solution {
    private int getIslands(char[][] grid, int i, int j, int m, int n, boolean[][] visited) {
        int right, left, up, down;
        if (i<0 || i>=m || j<0 || j>=n || grid[i][j]=='0' || visited[i][j])
            return 0;
        visited[i][j] = true;
        right = getIslands(grid, i, j+1, m, n, visited);
        left = getIslands(grid, i, j-1, m, n, visited);
        up = getIslands(grid, i+1, j, m, n, visited);
        down = getIslands(grid, i-1, j, m, n, visited);
        return 1;
    }

    public int numIslands(char[][] grid) {
        int islands = 0, m=grid.length, n=grid[0].length;
        boolean[][] visited = new boolean[m][n];

        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++)
                if (grid[i][j] != '0')
                    islands += getIslands(grid, i, j, m, n,visited);
        }
        return islands;
    }
}