package aoc2020;


import java.io.*;
import java.util.*;

public class aocday6 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("aocday6.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("aocday6.out")));

        ArrayList<Character> questions = new ArrayList<>();
        int sum = 0;
        String line = br.readLine();
        String line2;
        boolean first = true;

        while ((line != null)) {
            line2 = br.readLine();

            if (first) {
                for (int i = 0; i < line.length(); i++) {
                    questions.add(line.charAt(i));
                }
                first = false;

            } else {
                char[] c = line.toCharArray();
                ArrayList<Character> arrlist = new ArrayList<Character>();
                for (int n = 0; n < c.length; n++) {
                    arrlist.add(c[n]);
                }
               questions.retainAll(arrlist);

            }

            if ((line2 == null) || (line2.equals(""))) {
                first = true;
                sum += questions.size();
                System.out.println(questions);
                questions.clear();
                line2 = br.readLine();
            }
            
            line = line2;

        }

        pw.print(sum);
        pw.close();
        br.close();

    }
}
