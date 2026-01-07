import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int testCase = Integer.parseInt(br.readLine());
        StringTokenizer st;
        int repeatCount = 0;
        char[] sentence = new char[]{};
        String result = "";
        for(int i=0;i<testCase;i++){
            st = new StringTokenizer(br.readLine());
            repeatCount = Integer.parseInt(st.nextToken());
            sentence = st.nextToken().toCharArray();
            for(int j=0;j<sentence.length;j++){
                for(int k=0;k<repeatCount;k++){
                    result += sentence[j];
                }
            }

            System.out.println(result);
            result = "";

        }

    }
}