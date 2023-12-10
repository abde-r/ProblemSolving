public static void plusMinus(List<Integer> arr) {
    // Write your code here
        float p = arr.stream().filter(e -> e>0).count();
        float n = arr.stream().filter(e -> e<0).count();

        System.out.printf("%f\n %f\n %f\n", p/arr.size(), n/arr.size(), (arr.size()-(p+n))/arr.size());

}