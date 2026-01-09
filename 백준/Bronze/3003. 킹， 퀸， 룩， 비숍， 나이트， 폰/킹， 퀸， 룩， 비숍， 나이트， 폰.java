import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] chess = {1, 1, 2, 2, 2, 8};
        int[] result = new int[chess.length];

        StringTokenizer st = new StringTokenizer(br.readLine());

        while(st.hasMoreTokens()){
            for(int i=0;i<chess.length;i++){
                result[i] = chess[i] - Integer.parseInt(st.nextToken());
            }
        }

        for(int i=0;i<result.length;i++){
            System.out.print(result[i] + " ");
        }

    }

}