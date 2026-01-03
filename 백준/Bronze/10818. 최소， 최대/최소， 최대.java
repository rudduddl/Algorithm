import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;


public class Main {

    public static void main(String[] args) throws IOException{

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.parseInt(bf.readLine());
        StringTokenizer st = new StringTokenizer(bf.readLine());
        
        int min = 1000001;
        int max = -1000001;

        while(st.hasMoreTokens()){
            int current = Integer.parseInt(st.nextToken());
            if (current < min) min = current;
            if (current > max) max = current;
        }

        bw.write(min + " " + max);
        bw.flush();

    }
}