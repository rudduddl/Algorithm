import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int max = -1;
        int maxRow=0;
        int maxCol=0;
        
        for(int i=0;i<9;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j=0;j<9;j++){
                int value = Integer.parseInt(st.nextToken());
                if(max < value){
                    max = value;
                    maxRow = i+1;
                    maxCol = j+1;
                }
            }
        }
        System.out.println(max);
        System.out.println(maxRow + " " + maxCol);
    
        
    }

}

