public static String timeConversion(String s) {
    // Write your code here
        String[] t=s.split(":");
        
        String h=t[0];
        if (t[0].equals("12") && t[2].substring(2,4).equals("AM"))
            h = "00";
        else if (!t[0].equals("12") && t[2].substring(2,4).equals("PM"))
            h = Integer.toString((Integer.parseInt(t[0])+12)%24);

        return h+s.substring(2,s.length()-2);        
}