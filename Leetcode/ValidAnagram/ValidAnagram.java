class Solution {
    public boolean isAnagram(String s, String t) {
        char[] _s = s.toCharArray();
        char[] _t = t.toCharArray();

        Arrays.sort(_s);
        Arrays.sort(_t);

        return Arrays.equals(_s, _t);
    }
}