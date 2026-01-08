import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int maxNum = Integer.MIN_VALUE;

        StringBuilder sb = new StringBuilder();
        sb.append(br.readLine()).reverse().toString();
        StringTokenizer st = new StringTokenizer(sb.toString());

        while(st.hasMoreTokens()){
            int number = Integer.parseInt(st.nextToken());
            if(number > maxNum){
                maxNum = number;
            }
        }

        System.out.println(maxNum);

    }
}