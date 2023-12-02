class Solution {
    public int countCharacters(String[] words, String chars) {
        int count=0, j=0;
        for (int i=0; i<words.length; i++) {
            List<Character> temp = new ArrayList<Character>();
            for (Character c: chars.toCharArray())
                temp.add(c);
            for (j=0; j<words[i].length(); j++) {
                if (temp.indexOf(words[i].charAt(j))<0)
                    break;
                temp.remove(temp.indexOf(words[i].charAt(j)));
            }
            if (j==words[i].length())
                count+=j;
        }
        return count;
    }
}