import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int count = Integer.parseInt(br.readLine());
        boolean[][] paper = new boolean[100][100];
        int result = 0;

        for(int i=0;i<count;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int left = Integer.parseInt(st.nextToken());
            int right = Integer.parseInt(st.nextToken());

            for(int j=left;j<left+10;j++){
                for(int k=right;k<right+10;k++){
                    paper[j][k] = true;
                }
            }
            
        }

        for(int i=0;i<100;i++){
            for(int j=0;j<100;j++){
                if(paper[i][j] == true){
                    result += 1;
                }
            }
        }

        System.out.println(result);

    }

}
