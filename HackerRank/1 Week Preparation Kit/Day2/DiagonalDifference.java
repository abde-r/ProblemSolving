public static int diagonalDifference(List<List<Integer>> arr) {
    // Write your code here
        int s1=0, s2=0;
        for (int i=0; i<arr.size(); i++) {
            for (int j=0; j<arr.get(i).size(); j++) {
                if (i==j)
                    s1+=arr.get(i).get(j);
                if (arr.get(i).size()-i-1==j)
                    s2+=arr.get(i).get(j);
            }
        }
        return Math.abs(s1-s2);

}