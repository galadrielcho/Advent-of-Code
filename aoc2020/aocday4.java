import java.io.*;
import java.util.*;

public class aocday4 {
    public static ArrayList<String> lines;
    public static boolean[] necessities;
    public static int byr = 0, iyr = 1, eyr = 2, hgt = 3, hcl = 4, ecl = 5, pid = 6;
    public static String[] eclrs = new String[] {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"};
    public static void main(String[] args) throws IOException {
        lines = new ArrayList<String>();
        necessities = new boolean[7];
        BufferedReader br = new BufferedReader(new FileReader("aocday4.in"));
        PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("aocday4.out")));
        String line;

        int numvalid = 0;

        line = br.readLine();
        String line2;
        while (line != null) {
            line2 = br.readLine();
            lines.add(line);
            if (line2 == null || line.equals("")) {
                if (valid(lines)) {
                    numvalid++;
                }
                lines.clear();
            }
            line = line2;

        }

        pw.print(numvalid);
        pw.close();
        br.close();
    }

    public static boolean valid(ArrayList<String> lines) {
        for (String line : lines) {
            StringTokenizer st = new StringTokenizer(line);
            while (st.hasMoreTokens()) {
                String t = st.nextToken();
                String block = t.substring(0, 3);
                String block2 = t.substring(4, t.length());
                int num;
                
                if (block.equals("byr")) {
                    num = Integer.parseInt(block2);
                    necessities[byr] = num >= 1920 && num <= 2002;
                }

                else if (block.equals("iyr")) {
                    num = Integer.parseInt(block2);
                    necessities[iyr] = (num >= 2010 && num <= 2020);
                }
                else if (block.equals("eyr")) {
                    num = Integer.parseInt(block2);
                    necessities[eyr] = (num >= 2020 && num <= 2030);
                }
                else if (block.equals("hgt")) {
                    necessities[hgt] = hgt(block2);

                } 
                else if (block.equals("hcl")) {
                    necessities[hcl] = hcl(block2);
                }
                else if (block.equals("ecl")) {
                    necessities[ecl] = contains(eclrs, block2);
                }
                else if (block.equals("pid")) {
                    try {
                        Integer.parseInt(block2);
                        necessities[pid] = block2.length() == 9;
                    } catch (NumberFormatException ex) {

                    }
                }
                
            }

        }
        
        for (int i = 0; i < necessities.length; i++) {
            if (necessities[i] == false) {
                reset(necessities);
                return false;
            }
        }
        reset(necessities);
        return true;


    }

    public static void reset(boolean[] arr) {
        for (int i = 0; i < arr.length; i++) {
            arr[i] = false;
        }
    }

    public static boolean contains(String[] arr, String s) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i].equals(s))
                return true;
        }
        return false;
    }

    public static boolean hgt(String block2) {
        if (block2.contains("in")) {
            int block3 = Integer.parseInt(block2.substring(0, block2.length() - 2));
            return necessities[hgt] = block3 >= 59 && block3 <= 76;
        }
        else if (block2.contains("cm")) {
            int block3 = Integer.parseInt(block2.substring(0, block2.length() - 2));
            return block3 >= 150 && block3 <= 193;

        }

        return false;
    }

    public static boolean hcl(String block2) {
        if (block2.length() == 7) {
            if (block2.charAt(0) == '#') {
                for (int i = 1; i < block2.length(); i++) {
                    if (!((block2.charAt(i) >= '0' &&  block2.charAt(i) <= '9') || (block2.charAt(i) >= 'a' &&  block2.charAt(i) <= 'f'))) {
                        return false;
                    }
                }
                return true;
            }
        }

        return false;
    }

}
