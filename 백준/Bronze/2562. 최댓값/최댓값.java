import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

    public static void main(String[] args) throws IOException{

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int max = -1;
        int index = 0;

        for(int i=1;i<=9;i++){
            String line = bf.readLine();

            if(line == null || line.isEmpty()) break;

            int current = Integer.parseInt(line);

            if (current > max){
                max = current;
                index = i;
            }

        }

        bw.write(max + "\n" + index);
        bw.flush();

    }
}