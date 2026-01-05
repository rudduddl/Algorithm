import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        Integer t = Integer.parseInt(br.readLine());
        for (int i=0;i<t;i++){
            String message = br.readLine();
            bw.write(message.charAt(0) +""+ message.charAt(message.length()-1));
            bw.write("\n");
            
        }

        bw.flush();

    }
}