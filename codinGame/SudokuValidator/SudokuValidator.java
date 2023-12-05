import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        Set<String> s = new HashSet<>();
        int r=1;

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                int n = in.nextInt();
                if (!s.add("R"+i+"_"+n) || !s.add("C"+j+"_"+n) || !s.add("G"+"_"+n+"_"+i/3+j/3))
                    r=0;
            }
        }

        // Write an answer using System.out.println()
        // To debug: System.err.println("Debug messages...");

        if (r==1)
            System.out.println("true");
        else
            System.out.println("false");
    }
}