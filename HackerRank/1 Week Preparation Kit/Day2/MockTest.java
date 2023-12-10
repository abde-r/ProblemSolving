public static int flippingMatrix(List<List<Integer>> matrix) {
    // Write your code here
    int s=0, n=matrix.size();

    for (int i=0; i<n/2; i++) {
        for (int j=0; j<n/2; j++) {
            s += Math.max(matrix.get(i).get(j), Math.max(matrix.get(i).get(n-j-1), Math.max(matrix.get(n-i-1).get(j), matrix.get(n-i-1).get(n-j-1))));
        }
    }
    return s;
}