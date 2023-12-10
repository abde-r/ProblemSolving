public static void miniMaxSum(List<Integer> arr) {
    // Write your code here
        long sum= arr.stream().mapToLong(Integer::intValue).sum();
        int max = Collections.max(arr);
        int min = Collections.min(arr);
        
        System.out.printf("%d %d\n", sum-max, sum-min);
}