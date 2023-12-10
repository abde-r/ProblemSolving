public static int lonelyinteger(List<Integer> a) {
    // Write your code here
        for (int i: a)
            if (Collections.frequency(a, i)==1)
                return i;
        return 0;
}