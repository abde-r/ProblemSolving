import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {

    private static int GRID_SIZE = 9;
    private static boolean isNumberInRow(char[][] board, int row, char n) {
        for (int i=0; i<GRID_SIZE; i++)
            if (board[row][i]==n)
                return true;
        return false;
    }

    private static boolean isNumberInColumn(char[][] board, int column, char n) {
        for (int i=0; i<GRID_SIZE; i++)
            if (board[i][column]==n)
                return true;
        return false;
    }

    private static boolean isNumberInBox(char[][] board, int row, int column, char n) {
        int localBoxRow = row-row%3;
        int localBoxColumn = column-column%3;

        for (int i=localBoxRow; i<localBoxRow+3; i++) {
            for (int j=localBoxColumn; j<localBoxColumn+3; j++) {
                if (board[i][j]==n)
                    return true;
            }
        }
        return false;
    }

    private static boolean isValidPlacement(char[][] board, int row, int column, char n) {
        return !isNumberInRow(board, row, n) && !isNumberInColumn(board, column, n) && !isNumberInBox(board, row, column, n);
    }

    private static boolean solveBoard(char[][] board) {
        for (int row=0; row<GRID_SIZE; row++) {
            for (int column=0; column<GRID_SIZE; column++) {
                if (board[row][column]=='0') {
                    for (int numberToTry=1; numberToTry<=GRID_SIZE; numberToTry++) {
                        if (isValidPlacement(board, row, column, Character.forDigit(numberToTry, 10))) {
                            board[row][column]=Character.forDigit(numberToTry, 10);
                            if (solveBoard(board))
                                return true;
                            else
                                board[row][column]='0';
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String args[]) {
        char[][] board = new char[9][9];
        Scanner in = new Scanner(System.in);
        for (int i = 0; i < 9; i++) {
            String line = in.nextLine();
            for (int j=0; j<line.length(); j++)
                board[i][j] = line.charAt(j);
        }

        // Write an answer using System.out.println()
        // To debug: System.err.println("Debug messages...");

        solveBoard(board);
        for (int i = 0; i < GRID_SIZE; i++) {
            for (int j=0; j<GRID_SIZE; j++)
                System.out.print(board[i][j]);
            System.out.println();
        }
    }
}