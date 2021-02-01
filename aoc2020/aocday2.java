import java.io.*;
import java.util.*;

public class aocday2 {
    public static void main(String[] args) throws IOException {
        ArrayList<Integer> nums = new ArrayList<>();
        BufferedReader br = new BufferedReader(new FileReader("aocday2.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("aocday2.out")));
        String line;

        int valid = 0;
        while ((line = br.readLine()) != null) { 
            StringTokenizer st = new StringTokenizer(line);
            String[] limits = st.nextToken().split("-");
            Character letter = st.nextToken().charAt(0);
            String psw = st.nextToken();
            int pos1 = Integer.parseInt(limits[0]) - 1;
            int pos2 = Integer.parseInt(limits[1]) - 1;

            // int times = 0;
            // for (int i = 0; i < psw.length(); i++) {
            //     if (psw.charAt(i) == letter) {
            //         times++;
            //     }
            // }
            // if (times <= hi && times >= lo) {
            //     valid++;
            // }

            if ((psw.charAt(pos1) == letter && !(psw.charAt(pos2) == letter)) || (psw.charAt(pos2) == letter && !(psw.charAt(pos1) == letter))) {
                valid++;
            }
            
        }

        pw.print(valid);
        pw.close();
    }

}