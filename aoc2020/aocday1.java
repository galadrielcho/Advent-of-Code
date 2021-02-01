import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class aoc {
    public static void main(String[] args) throws IOException{
        ArrayList<Integer> nums = new ArrayList<>();
        BufferedReader br = new BufferedReader(new FileReader("stuff.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("stuff.out")));
        String line;
        while ((line = br.readLine()) != null) {
            StringTokenizer st = new StringTokenizer(line);
            nums.add(Integer.parseInt(st.nextToken()));
        }
        int mult = -1;
        for (int n : nums) {
            for (int j : nums) {
                for (int k : nums) {
                    if (j + n + k == 2020) {
                        mult = j*n*k;
                    }
                }
            }
        }
        pw.print(mult);
        pw.close();
        br.close();
    }
}
