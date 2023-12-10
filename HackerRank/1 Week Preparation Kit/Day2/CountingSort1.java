public static List<Integer> countingSort(List<Integer> arr) {
    // Write your code here
        Map<Integer, Integer> m = new HashMap<>();
        for (int i=0; i<100; i++)
            m.put(i, Collections.frequency(arr, i));
        
        List<Integer> t = new ArrayList<Integer>(m.values());
        return t;

}