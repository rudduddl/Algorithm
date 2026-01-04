import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        Set<Integer> setNumbers = new HashSet<>();

        for(int i=0;i<10;i++){
            setNumbers.add(Integer.parseInt(br.readLine())%42);
        }

        bw.write(String.valueOf(setNumbers.size()));
        bw.flush();
        
    }
}