import java.io.*;
import java.util.*;

public class aocday5 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("aocday5.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("aocday5.out")));
        ArrayList<Integer> ids = new ArrayList<>();
        String line;
        int sid;
        while ((line = br.readLine()) != null) {
            ids.add(getSeatID(line));
        }

        Collections.sort(ids);

        for(int a = 0; a < ids.size() - 1; a++) {
            if (ids.get(a+1) - ids.get(a) != 1) {
                pw.println(ids.get(a+1) + " " + ids.get(a));

            }
        }

        pw.close();
        br.close();
    }

    public static int getSeatID(String s) {
        int pos = -1;
        int hi = 127;
        int lo = 0;

        for (int i = 0; i < 7; i++) {
            char c = s.charAt(i);
            if (c == 'F') {
                hi = (hi - 1 - lo) / 2 + lo;
            } else if (c == 'B') {
                lo = (hi + 1 - lo) / 2 + lo;
            }
        }

        int row = lo;

        hi = 7;
        lo = 0;

        for (int j = 7; j < 10; j++) {
            char c = s.charAt(j);
            if (c == 'L') {
                hi = (hi - 1 - lo) / 2 + lo;
            } else if (c == 'R') {
                lo = (hi + 1 - lo) / 2 + lo;
            }
        }

        return (row * 8) + lo;

    }
}
