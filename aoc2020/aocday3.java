import java.io.*;
import java.util.*;


public class aocday3 {
    public static ArrayList<String> lines;
    public static void main(String[] args) throws IOException{
        lines = new ArrayList<>();
        BufferedReader br = new BufferedReader(new FileReader("aocday3.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("aocday3.out")));
        String line;

        
        while ((line = br.readLine()) != null) {
            lines.add(line);
        }
        int a = count(1, 1);
        int b = count(3, 1);
        int c = count(5, 1);
        int d = count(7, 1);
        int e = count(1, 2);
        System.out.println(a + " " + b + " " + " " + c + " " + d + " " + e);
        pw.print(a * b * c * d * e);
        pw.close();
    }

    public static int count(int right, int down) {
        int pos = 0;
        int trees = 0;
        int l = 0;
        int r = right;
        int d = down;

        int i =0;        
       while ( i < lines.size()) {
            if (lines.get(i).charAt(pos % lines.get(i).length()) == '#') {
                trees++;
            }
            
            pos += r;
            i += d;


        }
        return trees;
    }
}